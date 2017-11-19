import socket, sys
import struct

import yaml
from struct import *

from network.NetworkUtils import serializeIPHeader, checksum
from network.OSPFSerializer import serializeOSPFHelloHeader, serializeOSPFDatabaseHeader
from packet.OSPFDatabaseDescriptorHeader import OSPFDatabaseDescriptorHeader
from packet.OSPFHelloHeader import OSPFHelloHeader

def create_dd_update(router_id, area_id):
    dd_update = OSPFDatabaseDescriptorHeader(2, 32, router_id, area_id, 0, 0, 0, 0, 1)

    return dd_update

def createHelloPacket(router_id, area_id, network_mask, hello_interval, router_dead_interval):
    hello_packet = OSPFHelloHeader(2, 48, router_id, area_id, 0, 0, 0,
                                                    network_mask, hello_interval, 255, router_dead_interval,
                                                    "0.0.0.0", "0.0.0.0", "0.0.0.0")
    hello_packet.set_option_mc(True)
    return hello_packet


def main():
    # open configuration file
    with open("config.yml", 'r') as ymlfile:
        config = yaml.load(ymlfile)

    MCAST_GRP = '224.0.0.1'
    MCAST_PORT = 10000

    # initialize the socket
    try:
        sfd = socket.socket(socket.AF_INET, socket.SOCK_RAW, 89)
        ttl = struct.pack('b', 1)
        sfd.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

        hello = createHelloPacket('192.168.1.9', "0.0.0.0", '255.255.255.0', 10, 40)
        dd_update = create_dd_update('192.168.1.9', "0.0.0.0")

        for i in range(1, 1000, 1):
            print sfd.sendto(serializeOSPFHelloHeader(hello), (MCAST_GRP, MCAST_PORT))
            print sfd.sendto(serializeOSPFDatabaseHeader(dd_update), (MCAST_GRP, MCAST_PORT))
            dd_update.increment_sequence()

    except socket.error, msg:
        print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()


if __name__ == "__main__":
    main()
