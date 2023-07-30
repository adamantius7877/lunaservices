from Common.enums.ServiceEnums import MessageType
from Common.MessageFactory import MessageFactory 
from Common import Processing_Channel, Logging_Channel, Storage_Channel, Registration_Channel, SpeechToText_Channel, TextToSpeech_Channel
from Models.LunaConfiguration import LunaConfiguration
from Models.LunaObject import LunaObject
import redis, threading

class BaseService(LunaObject):
    '''This is an abstract base class used to define the basics of a service component in the LUNA system'''

    def __init__(self, serviceType):
        super().__init__()
        self.ServiceType = serviceType
        self.Nodes = {} 
        print(f"{str(self.ServiceType)} loaded")

    def AddNode(self, nodeId, callback):
        if nodeId not in self.Nodes:
            self.Nodes.update({nodeId:threading.Thread(target=callback, args=(nodeId,), daemon=True).start()})
            print("Adding node: " + nodeId)

    def RemoveNode(self, nodeId):
        if nodeId in self.Nodes:
            self.Nodes[nodeId].stop()
            self.Nodes.pop(nodeId)
            print("Removing node: " + nodeId)
