from OSPFHeader import OSPFHeader


# Network mask               (OSPFv2 only) Network mask associated with the interface.
# Hello interval             How often the router sends hello Headers. All routers on a shared network must use the same
#                            hello interval.
# Options                    Optional capabilities of the router.
# Router priority            The router's priority to become the designated router.
# Router dead interval       How long the router waits without receiving any OSPF Headers from a router before declaring
#                            that router to be down. All routers on a shared network must use the same router dead
#                            interval.
# Designated router          IP address of the designated router.
# Backup designated router   IP address of the backup designated router.
# Neighbor                   IP addresses of the routers from which valid hello Headers have been received within the
#                            time specified by the router dead interval.
class OSPFDatabaseDescriptorHeader(OSPFHeader):
    def __init__(self, version, length, router_id, area_id, auth_type, authentication1, authentication2,
               interface_mtu, dd_sequence_number):
        super(OSPFDatabaseDescriptorHeader, self).__init__(version, 0, 2, length, router_id, area_id, auth_type,
                                              authentication1, authentication2)
        self.interface_mtu = interface_mtu
        self.dd_sequence_number = dd_sequence_number
        self.options = 0
        self.control_bits = 0

    '''
    DN-bit
    '''
    def set_option_dn(self, value):
        if value:
            self.options |= 128
        else:
            self.options &= 127

    '''
    O-bit
    '''
    def set_option_o(self, value):
        if value:
            self.options |= 64
        else:
            self.options &= 191

    '''
    Demand circuits support
    '''
    def set_option_dc(self, value):
        if value:
            self.options |= 32
        else:
            self.options &= 223

    '''
    Packet contains a LLS data block
    '''
    def set_option_l(self, value):
        if value:
            self.options |= 16
        else:
            self.options &= 239

    '''
    NSSA support
    '''
    def set_option_np(self, value):
        if value:
            self.options |= 8
        else:
            self.options &= 247

    '''
    Multicast capability
    '''
    def set_option_mc(self, value):
        if value:
            self.options |= 4
        else:
            self.options &= 251

    '''
    External routing capability
    '''
    def set_option_e(self, value):
        if value:
            self.options |= 2
        else:
            self.options &= 253

    '''
    Multi-Topology capability
    '''
    def set_option_e(self, value):
        if value:
            self.options |= 1
        else:
            self.options &= 254

    '''
    Set the initial bit
    '''
    def set_control_initial_bit(self, value):
        if value:
            self.control_bits |= 4
        else:
            self.control_bits &= 251

    '''
    Set the more packets bit
    '''
    def set_control_more_bit(self, value):
        if value:
            self.control_bits |= 2
        else:
            self.control_bits &= 253

    '''
    Set the initial bit
    '''
    def set_control_master_slave_bit(self, value):
        if value:
            self.control_bits |= 1
        else:
            self.control_bits &= 254

    def set_sequence_number(self, value):
        self.dd_sequence_number = value

    def increment_sequence(self):
        self.dd_sequence_number += 1
