from .GraphDataObject import GraphNode
from Common.enums import GraphNodeType

#rooms contain nodes and are part of groups and properties
class LunaRoom(GraphNode):

    def __ini__(self):
        super(Room, self).__ini__(GraphNodeType.ROOM)
        self.Name = ""


