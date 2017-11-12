from struct import *
import socket

def checksum(msg):
    s = 0
    # loop taking 2 characters at a time
    for i in range(0, len(msg), 2):
        w = ord(msg[i]) + (ord(msg[i + 1]) << 8)
        s = s + w

    s = (s >> 16) + (s & 0xffff);
    s = s + (s >> 16);

    # complement and mask to 4 byte short
    s = ~s & 0xffff

    return s

def serializeIPHeader(ip_id, ip_proto, source_ip, dest_ip):
    # ip header fields
    ip_ihl = 5
    ip_ver = 4
    ip_tos = 0
    ip_tot_len = 0  # kernel will fill the correct total length
    ip_frag_off = 0
    ip_ttl = 255
    ip_check = 0  # kernel will fill the correct checksum
    ip_saddr = socket.inet_aton(source_ip)
    ip_daddr = socket.inet_aton(dest_ip)

    ip_ihl_ver = (ip_ver << 4) + ip_ihl

    # the ! in the pack format string means network order
    return pack('!BBHHHBBH4s4s',
                     ip_ihl_ver,
                     ip_tos,
                     ip_tot_len,
                     ip_id,
                     ip_frag_off,
                     ip_ttl,
                     ip_proto,
                     ip_check,
                     ip_saddr,
                     ip_daddr)

def serializeTCPHeader(tcp_source, tcp_dest, tcp_seq, tcp_ack_seq, tcp_fin, tcp_syn, tcp_rst, tcp_psh, tcp_ack, tcp_urg, source_ip, dest_ip, data):
    # tcp header fields
    tcp_doff = 5  # 4 bit field, size of tcp header, 5 * 4 = 20 bytes
    tcp_window = socket.htons(5840)  # maximum allowed window size
    tcp_check = 0
    tcp_urg_ptr = 0

    tcp_offset_res = (tcp_doff << 4) + 0
    tcp_flags = tcp_fin + (tcp_syn << 1) + (tcp_rst << 2) + (tcp_psh << 3) + (tcp_ack << 4) + (tcp_urg << 5)

    # the ! in the pack format string means network order
    tcp_header = pack('!HHLLBBHHH', tcp_source, tcp_dest, tcp_seq, tcp_ack_seq, tcp_offset_res, tcp_flags, tcp_window,
                      tcp_check, tcp_urg_ptr)

    # pseudo header fields
    source_address = socket.inet_aton(source_ip)
    dest_address = socket.inet_aton(dest_ip)
    placeholder = 0
    protocol = socket.IPPROTO_TCP
    tcp_length = len(tcp_header) + len(data)

    psh = pack('!4s4sBBH', source_address, dest_address, placeholder, protocol, tcp_length);
    psh = psh + tcp_header + data;

    tcp_check = checksum(psh)
    # print tcp_checksum

    # make the tcp header again and fill the correct checksum - remember checksum is NOT in network byte order
    return pack('!HHLLBBH',
                tcp_source,
                tcp_dest,
                tcp_seq,
                tcp_ack_seq,
                tcp_offset_res,
                tcp_flags,
                tcp_window) \
           + pack('H', tcp_check) \
           + pack('!H', tcp_urg_ptr)

