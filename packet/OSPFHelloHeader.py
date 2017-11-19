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
class OSPFHelloHeader(OSPFHeader):
    def __init__(self, version, length, router_id, area_id, auth_type, authentication1, authentication2,
               network_mask, hello_interval, router_priority, router_dead_interval,
               designated_router, backup_designated_router, neighbor):
        super(OSPFHelloHeader, self).__init__(version, 0, 1, length, router_id, area_id, auth_type,
                                              authentication1, authentication2)
        self.networkMask = network_mask
        self.helloInterval = hello_interval
        self.options = 0
        self.routerPriority = router_priority
        self.routerDeadInterval = router_dead_interval
        self.designatedRouter = designated_router
        self.backupDesignatedRouter = backup_designated_router
        self.neighbor = neighbor

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