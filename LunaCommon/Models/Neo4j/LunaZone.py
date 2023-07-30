from .GraphDataObject import GraphNode
from Common.enums import GraphNodeType

# zones can be zoned and grouped, they are a part of properties
class LunaZone(GraphNode):
    
    def __init__(self):
        super().__init__(GraphNodeType.ZONE)
        self.Tags = []
