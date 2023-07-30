from .GraphDataObject import GraphNode
from Common.enums import BlueprintType, BlueprintSubType, GraphNodeType

# a blueprint is the foundation of commands in the system
# a blueprint is all the information required to be able to 
# effectively run a command or the ability to aquire said information
# if the information is not available immediately.  This includes
# the ability (through relationships) to be able to formulate questions
# to ask the user to continue building the blueprint further 
class LunaBlueprint(GraphNode):
    
    def __init__(self):
        super().__init__(GraphNodeType.BLUEPRINT)
        self.BlueprintType = BlueprintType.Command
        self.BlueprintSubType = BlueprintSubType.NONE
        self.Params = {} 
