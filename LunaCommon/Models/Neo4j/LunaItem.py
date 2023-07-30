from .GraphDataObject import GraphRelationship
from Common.enums import GraphRelationshipType

# the item that receives the action a device can perform and is tied to a blueprint
class LunaItem(GraphRelationship):
    
    def __init__(self):
        super().__init__(GraphRelationshipType.ITEM_OF)
        self.Tags = []
