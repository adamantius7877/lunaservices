from Common.enums import MessageType, MessageSubType

def LunaMessageBase(object):

    def __init__(self):
        self.MessageType = MessageType.Command
        self.MessageSubType = MessageSubType.NONE
        self.UserToken = ""
        self.Data = {}
