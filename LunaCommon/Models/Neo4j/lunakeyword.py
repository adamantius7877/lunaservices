from .GraphDataObject import GraphNode
from Common.enums import GraphNodeType

# a keyword is tied to blueprints by relationships: conditionals, items, and directives
class LunaKeyword(GraphNode):
    
    def __init__(self):
        super().__init__(GraphNodeType.KEYWORD)
        self.Tags = []
