from Common.enums.ServiceEnums import MessageType
from Common.MessageFactory import MessageFactory
from Common.GraphDataModule import GraphDataModule
from Common import Processing_Channel, Logging_Channel, Storage_Channel, Registration_Channel, SpeechToText_Channel, TextToSpeech_Channel, Questions_Channel
from Models.LunaConfiguration import LunaConfiguration
from Messages.LunaMessage import LunaMessage
import redis, threading, json, socket

class LunaObject(object):
    '''This is an abstract base class used to define the basics of an object in the LUNA system'''

    def __init__(self):
        self.Configuration = LunaConfiguration()
        primaryQueue = self.Configuration.LoadedConfiguration.RedisQueues['primary']
        self.Redis = redis.Redis(host=primaryQueue.Server, port=primaryQueue.Port)
        self.RedisPubSub = self.Redis.pubsub()
        self.MessageFactory = MessageFactory()
        dbInfo = self.Configuration.LoadedConfiguration.Neo4jConnectionStrings["primary"]
        self.GraphModule = GraphDataModule(dbInfo)

    def StartRedis(self):
        self.RedisThread = self.RedisPubSub.run_in_thread(sleep_time=0.001)

    def PublishToProcessing(self, data):
        self.Redis.publish(Processing_Channel, data.toJSON())

    def PublishToLogging(self, data):
        self.Redis.publish(Logging_Channel, data.toJSON())

    def PublishToStorage(self, data):
        self.Redis.publish(Storage_Channel, data.toJSON())

    def PublishToTextToSpeech(self, data):
        self.Redis.publish(TextToSpeech_Channel, data.toJSON())

    def PublishToSpeechToText(self, data):
        self.Redis.publish(SpeechToText_Channel, data.toJSON())

    def PublishToQuestions(self, data):
        self.Redis.publish(Questions_Channel, data.toJSON())

    def PublishToRegistration(self, data):
        self.Redis.publish(Registration_Channel, data.toJSON())

    def PublishToNode(self, data):
        self.Redis.publish(data.NodeId, data.toJSON())

    def PublishToNodeRegistration(self, data):
        self.Redis.publish(f'{data.NodeId}:{Registration_Channel}', data.toJSON())

    def UnsubscribeFromChannel(self, channel):
        self.RedisPubSub.unsubscribe(channel)

    def SubscribeToChannel(self, channel, callback):
        self.RedisPubSub.subscribe(**{channel:callback})

    def SubscribeToRegistration(self, callback):
        self.SubscribeToChannel(Registration_Channel, callback)

    def SubscribeToProcessing(self, callback):
        self.SubscribeToChannel(Processing_Channel, callback)

    def SubscribeToLogging(self, callback):
        self.SubscribeToChannel(Logging_Channel, callback)
        
    def SubscribeToStorage(self, callback):
        self.SubscribeToChannel(Storage_Channel, callback)

    def SubscribeToTextToSpeech(self, callback):
        self.SubscribeToChannel(TextToSpeech_Channel, callback)

    def SubscribeToSpeechToText(self, callback):
        self.SubscribeToChannel(SpeechToText_Channel, callback)

    def SubscribeToQuestions(self, callback):
        self.SubscribeToChannel(Questions_Channel, callback)

    def SpeakToNode(self, text, nodeId):
        print(f"Saying {text}")
        self.PublishToTextToSpeech(self.MessageFactory.GetBaseMessage(MessageType.TextToSpeech, text, nodeId))
    
    def Log(self, data):
        self.PublishToLogging(data)

    def GetMessage(self, rawMessage):
        if isinstance(rawMessage, LunaMessage):
            message = rawMessage
        else:
            message = LunaMessage()
            json_data = json.loads(rawMessage["data"].decode('utf-8'))
            message.FromJson(json_data)

        return message

    def GetHostName(self):
        return socket.gethostname()

    def GetIp(self):
        return socket.gethostbyname(self.GetHostName()) 

