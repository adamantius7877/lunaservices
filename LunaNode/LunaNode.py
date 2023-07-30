from Common.enums.ServiceEnums import MessageType
from Common.enums import MessageType, NodeStatus
from Common.MessageFactory import MessageFactory
from Common import Processing_Channel, Logging_Channel, Storage_Channel, Registration_Channel, SpeechToText_Channel, TextToSpeech_Channel, Heartbeat_Channel
from Models.LunaConfiguration import LunaConfiguration
from Models.LunaObject import LunaObject
from Models import Data
from Modules.ListeningModule import LunaListen
from Modules.RegistrationModule import LunaNodeRegistrationModule
from random import randrange
import simpleaudio as sa
import uuid, threading, time

class BaseNode(LunaObject):
    def __init__(self, name):
        super().__init__()
        self.Load(name)

    def Load(self, name):
        self.LoadNodeId()
        self.RegistrationModule = LunaNodeRegistrationModule(self)
        self.NodeMouthChannel = f'{self.NodeId}:{TextToSpeech_Channel}'
        self.NodeRegistrationChannel = f'{self.NodeId}:{Registration_Channel}'
        self.NodeHeartbeatChannel = f'{self.NodeId}:{Heartbeat_Channel}'
        self.SubscribeToChannels()
        self.Name = name 
        self.Lock = threading.Lock()
        self.RegistrationModule.Register()
        self.SetStatus(NodeStatus.Active)
        self.ListenModule = LunaListen(self)

    def LoadNodeId(self):
        self.NodeId = self.Configuration.LoadedConfiguration.NodeId 
        if self.NodeId == "":
            self.SetNodeId(str(uuid.uuid1()))
        print(f"NodeId: {self.NodeId}")

    def SetStatus(self, status):
        self.Status = status

    def UnsubscribeFromChannels(self):
        try:
            self.UnsubscribeFromChannel(self.NodeRegistrationChannel)
            self.UnsubscribeFromChannel(self.NodeMouthChannel)
        except:
            pass

    def SubscribeToChannels(self):
        self.SubscribeToChannel(self.NodeRegistrationChannel, self.RegistrationModule.NodeRegisterResponse)
        self.SubscribeToChannel(self.NodeMouthChannel, self.PlayLuna)
        self.StartRedis()

    def SetNodeId(self, nodeId):
        self.UnsubscribeFromChannels()
        self.NodeId = nodeId
        self.Configuration.LoadedConfiguration.NodeId = nodeId
        self.Configuration.SaveConfiguration()
        self.NodeMouthChannel = f'{self.NodeId}:{TextToSpeech_Channel}'
        print(f'{self.NodeMouthChannel}')
        self.NodeRegistrationChannel = f'{self.NodeId}:{Registration_Channel}'
        self.NodeHeartbeatChannel = f'{self.NodeId}:{Heartbeat_Channel}'
        self.SubscribeToChannels()

    def SendRawAudio(self, data):
        #self.PublishMessage(self.NodeId + ":rawaudio", data, CommandType.RawAudio)
        #print("Sending raw audio to channel " + self.NodeId + ":rawaudio")
        self.Redis.publish(f"{self.NodeId}:{SpeechToText_Channel}", data)
        #self.Redis.publish(self.NodeId + ":rawaudio", data)

    def Speak(self, text):
        self.SpeakToNode(text, self.NodeId)

    def PlayAudio(self, data):
        threading.Thread(target=self.PlayLuna, args=(data,), daemon=True).start()
        print(f"Speaking audio received")

    def PlayLuna(self, data):
        with self.Lock:
            message = bytearray(data["data"])
            channels = 1
            sampleWidth = 2
            frequencyRate = 22050
            playObj = sa.play_buffer(message, channels, sampleWidth, frequencyRate)
            playObj.wait_done()

    def GetGreeting(self):
        greetings = ['Online']
        return greetings[randrange(len(greetings))]

class LunaNode(BaseNode):

    def __init__(self, name):
        super().__init__(name)


#node = LunaNode("test")
#test = input()
