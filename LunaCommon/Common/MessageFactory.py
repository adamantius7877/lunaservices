from Messages.LunaMessage import LunaMessage
from Common.enums.ServiceEnums import MessageType
from datetime import datetime

class MessageFactory(object):

    def __init__(self):
        pass

    def GetStorageMessage(self, data, nodeId):
        return self.GetBaseMessage(MessageType.Storage, data, nodeId)

    def GetLoggingMessage(self, data, nodeId):
        return self.GetBaseMessage(MessageType.Logging, data, nodeId)

    def GetRegistrationMessage(self, data, nodeId):
        return self.GetBaseMessage(MessageType.Registration, data, nodeId)

    def GetTextProcessingMessage(self, data, nodeId):
        return self.GetBaseMessage(MessageType.TextProcessing, data, nodeId)

    def GetCommandProcessingMessage(self, data, nodeId):
        return self.GetBaseMessage(MessageType.CommandProcessing, data, nodeId)

    def GetTextToSpeechMessage(self, data, nodeId):
        return self.GetBaseMessage(MessageType.TextToSpeech, data, nodeId)

    def GetSpeechToTextMessage(self, data, nodeId):
        return self.GetBaseMessage(MessageType.SpeechToText, data, nodeId)

    def GetBaseMessage(self, messageType, data, nodeId):
        message = LunaMessage()
        message.NodeId = nodeId
        message.TimeStamp = datetime.now().strftime("%H:%M:%S")
        message.Data = data
        message.MessageType = messageType
        return message
