from .GraphDataObject import GraphNode
from Common.enums import GraphNodeType

# a device has capabilities and is tied to a node
class LunaDevice(GraphNode):
    
    def __init__(self):
        super().__init__(GraphNodeType.DEVICE)
        self.DeviceId = ""
        self.Node = ""
        self.Capabilities = []
