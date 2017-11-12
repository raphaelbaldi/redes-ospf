
'''
Version:        The current OSPF version number. This can be either 2 or 3.
Type:           Type of OSPF Header.
Length          Length of the Header, in bytes, including the header.
RouterID        IP address of the router from which the Header originated.
AreaID          Identifier of the area in which the Header is traveling. Each OSPF Header is associated with a single area. Headers traveling over a virtual link are labeled with the backbone area ID, 0.0.0.0. .
Checksum        Fletcher checksum.
Authentication  (OSPFv2 only) Authentication scheme and authentication information.
InstanceID      (OSPFv3 only) Identifier used when there are multiple OSPFv3 realms configured on a link.
'''
class OSPFHeader:
    def __init__(self, version, type, length, routerID, areaID, checksum, authType, authentication1, authentication2, instanceID):
        self.version = version
        self.type = type
        self.length = length
        self.routerID = routerID
        self.areaID = areaID
        self.checksum = checksum
        self.authType = authType
        self.authentication1 = authentication1
        self.authentication2 = authentication2
        self.instanceID = instanceID

    def Code(self):
        return self.code