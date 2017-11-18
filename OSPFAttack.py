import socket, sys
import struct

import yaml
from struct import *

from network.NetworkUtils import serializeIPHeader
from network.OSPFSerializer import serializeOSPFHelloHeader
from packet.OSPFHelloHeader import OSPFHelloHeader


def createHelloPacket(router_id, area_id, network_mask, hello_interval, router_dead_interval):
    return serializeOSPFHelloHeader(OSPFHelloHeader(4, 48, router_id, area_id, 0, 0, 0,
                           network_mask, hello_interval, 0, 1, router_dead_interval,
                           '0.0.0.0', '0.0.0.0', '0.0.0.0'))

def main():
    # open configuration file
    with open("config.yml", 'r') as ymlfile:
        config = yaml.load(ymlfile)

    # initialize the socket
    try:
        sfd = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        ttl = struct.pack('b', 1)
        sfd.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

        ip = serializeIPHeader(0, 5, '192.168.1.9', '224.0.0.5')
        hello = createHelloPacket(3200, 0, '255.255.255.0', 10, 40)

        for i in range(1, 10000000, 1):
            print sfd.sendto(ip + hello, ('224.0.0.5', 1000))

    except socket.error , msg:
        print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()


if __name__ == "__main__":
    main()