from Common.enums.StorageEnums import StorageType
class DataMessage(object):

    def __init__(self):
        self.Data = []

class LoggingDataMessage(DataMessage):

    def __init__(self):
        super.__init__()
        self.LoggingType = StorageType.Service

class StorageDataMessage(DataMessage):

    def __init__(self):
        super.__init__()
        self.StorageType = StorageType.Node
