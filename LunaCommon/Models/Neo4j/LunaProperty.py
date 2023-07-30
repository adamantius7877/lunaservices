from .GraphDataObject import GraphNode
from Common.enums import GraphNodeType

#properties have Groups, zones, rooms and are owned by owners, used by users

class LunaProperty(GraphNode):
    
    def __init__(self):
        super().__init__(GraphNodeType.PROPERTY)
        self.Tags = []
