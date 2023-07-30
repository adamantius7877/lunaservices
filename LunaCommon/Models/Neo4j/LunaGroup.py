from .GraphDataObject import GraphNode
from Common.enums import GraphNodeType

# Items that can be grouped 
# Name, Groups, Zones, Rooms, Properties
class LunaGroup(GraphNode):
    
    def __init__(self):
        super().__init__(GraphNodeType.GROUP)
        self.Tags = []
