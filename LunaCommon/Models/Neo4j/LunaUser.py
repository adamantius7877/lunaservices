from .GraphDataObject import GraphNode
from Common.enums import GraphNodeType

# a user is tied to the properties, owned properties, rooms, groups, and nearly everything
# in the system, this will have to be modified to handle the numerous amounts 
# of relationships this might have in the system
class LunaUser(GraphNode):
    
    def __init__(self):
        super().__init__(GraphNodeType.USER)
        self.Tags = []