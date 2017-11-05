import OSPFPacket

'''
Network mask                (OSPFv2 only) Network mask associated with the interface.
Hello interval              How often the router sends hello packets. All routers on a shared network must use the same hello interval.
Options                     Optional capabilities of the router.
Router priority             The router’s priority to become the designated router.
Router dead interval        How long the router waits without receiving any OSPF packets from a router before declaring that router to be down. All routers on a shared network must use the same router dead interval.
Designated router           IP address of the designated router.
Backup designated router    IP address of the backup designated router.
Neighbor                    IP addresses of the routers from which valid hello packets have been received within the time specified by the router dead interval.
'''
class OSPFHelloPacket(OSPFPacket):
    def __init(self, version, length, routerID, areaID, checksum, authType, authentication1, authentication2, instanceID,
               networkMask, helloInterval, options, routerPriority, routerDeadInterval, designatedRouter, backupDesignatedRouter, neighbor):
        OSPFPacket.__init__(version, 1, length, routerID, areaID, checksum, authType, authentication1, authentication2, instanceID)
        self.networkMask = networkMask
        self.helloInterval = helloInterval
        self.options = options
        self.routerPriority = routerPriority
        self.routerDeadInterval = routerDeadInterval
        self.designatedRouter = designatedRouter
        self.backupDesignatedRouter = backupDesignatedRouter
        self.neighbor = neighbor
