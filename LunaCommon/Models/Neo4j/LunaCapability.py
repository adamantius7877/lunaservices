from .GraphDataObject import GraphRelationship
from Common.enums import GraphRelationshipType

# a capability the action a device can perform and is tied to a blueprint
class LunaCapability(GraphRelationship):
    
    def __init__(self):
        super().__init__(GraphRelationshipType.CAPABLE_OF)
        self.Tags = []
