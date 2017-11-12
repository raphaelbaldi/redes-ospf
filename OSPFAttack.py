import socket, sys
import yaml
from struct import *

def main():
    # open configuration file
    with open("config.yml", 'r') as ymlfile:
        config = yaml.load(ymlfile)

    # initialize the socket
    try:
        sfd = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    except socket.error , msg:
        print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

    #sfd.sendto(packet, (dest_ip, 0))



if __name__ == "__main__":
    main()