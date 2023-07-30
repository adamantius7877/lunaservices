from Common.enums import GraphNodeType, GraphRelationshipType, BlueprintType, BlueprintSubType, ServiceEnums, StorageEnums

class Blueprint(object):

    def __init__(self):
        self.BlueprintType = BlueprintType.Command
        self.BlueprintSubType = BlueprintSubType.NONE

class BlueprintStep(object):

    def __init__(self):
        self.BlueprintType = BlueprintType.Command
