# Version:        The current OSPF version number. This can be either 2 or 3.
# Type:           Type of OSPF Header.
# Length          Length of the Header, in bytes, including the header.
# RouterID        IP address of the router from which the Header originated.
# AreaID          Identifier of the area in which the Header is traveling. Each OSPF Header is associated with a single
#                area. Headers traveling over a virtual link are labeled with the backbone area ID, 0.0.0.0. .
# Checksum        Fletcher checksum.
# Authentication  (OSPFv2 only) Authentication scheme and authentication information.
# InstanceID      (OSPFv3 only) Identifier used when there are multiple OSPFv3 realms configured on a link.
class OSPFHeader(object):
    def __init__(self, version, code, header_type, length, router_id, area_id, auth_type, authentication1,
                 authentication2):
        self.version = version
        self.code = code
        self.header_type = header_type
        self.length = length
        self.routerID = router_id
        self.areaID = area_id
        self.checksum = 0  # computed later
        self.authType = auth_type
        self.authentication1 = authentication1
        self.authentication2 = authentication2

    def set_code(self, code):
        self.code = code
