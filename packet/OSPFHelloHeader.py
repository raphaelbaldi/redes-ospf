import OSPFHeader


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
    def __init(self, version, length, router_id, area_id, checksum, auth_type, authentication1, authentication2,
               instance_id, network_mask, hello_interval, options, router_priority, router_dead_interval,
               designated_router, backup_designated_router, neighbor):
        super(OSPFHelloHeader, self).__init__(version, 0, 1, length, router_id, area_id, checksum, auth_type,
                                              authentication1, authentication2, instance_id)
        self.networkMask = network_mask
        self.helloInterval = hello_interval
        self.options = options
        self.routerPriority = router_priority
        self.routerDeadInterval = router_dead_interval
        self.designatedRouter = designated_router
        self.backupDesignatedRouter = backup_designated_router
        self.neighbor = neighbor
