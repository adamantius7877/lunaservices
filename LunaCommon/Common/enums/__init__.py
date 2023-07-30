from enum import Enum, IntEnum
from .BlueprintType import BlueprintType
from .LoggingEnums import LoggingType
from .ServiceEnums import MessageType, ServiceType
from .StorageEnums import StorageType, StorageSubType
from .MessageType import MessageType 
from .MessageSubType import MessageSubType
from .DataType import DataType 
from .NodeStatus import NodeStatus

class NoValue(Enum):
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)

class BlueprintSubType(IntEnum):
    NONE = 0,
    SYSTEM = 1,
    AUTOMATION = 2,
    WEBREQUEST = 3,
    LIST = 4,
    REMINDER = 5,

class GraphNodeType(NoValue):
    BLUEPRINT = "LunaBlueprint",
    KEYWORD = "LunaKeyword",
    USER = "LunaUser",
    GROUP = "LunaGroup",
    ROOM = "LunaRoom",
    ZONE = "LunaZone",
    PROPERTY = "LunaProperty",
    NODE = "LunaNode",
    DEVICE = "LunaDevice",
    STEP = "BlueprintStep",
    CONDITIONAL = "LunaConditional",

class GraphRelationshipType(NoValue):
    DIRECTIVE_OF = "DIRECTIVE_OF",
    ITEM_OF = "ITEM_OF",
    CONDITIONAL_OF = "CONDITIONAL_OF",
    OWNER_OF = "OWNER_OF",
    ZONE_OF = "ZONE_OF",
    OWNED_BY = "OWNED_BY",
    CAN_USE = "CAN_USE",
    USER_OF = "USER_OF",
    GROUPED_TO = "GROUPED_TO",
    GROUP_OF = "GROUP_OF",
    ZONED_TO = "ZONED_TO",
    CONTAINED_IN = "CONTAINED_IN",
    DEVICE_OF = "DEVICE_OF",
    CAPABLE_OF = "CAPABLE_OF",
    STEP_OF = "STEP_OF",


