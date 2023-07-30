from Models.BaseService import BaseService
from Common.enums import ServiceEnums
from Common import SpeechToText_Channel
from vosk import KaldiRecognizer, Model, SetLogLevel
import threading, json 

class SpeechToTextService(BaseService):

    def __init__(self):
        super().__init__(ServiceEnums.ServiceType.SpeechToText)
        self.Lock = threading.Lock()
        SetLogLevel(-1)
        self.Rate = 44100
        self.Model = Model("model")
        self.Rec = KaldiRecognizer(self.Model, self.Rate)
        self.SubscribeToSpeechToText(self.AddRegisteredNode)
        self.StartRedis()
        self.IsListening = False

    def AddRegisteredNode(self, rawmessage):
        message = self.GetMessage(rawmessage)
        self.AddNode(message.NodeId, self.SubscribeToNodeAudio)

    def ProcessRawAudio(self, data, node):
        if data["data"] is not bytearray:
            in_data = bytes(data["data"])
        else:
            in_data = data["data"]
        try:
            if len(in_data) > 0 and self.Rec.AcceptWaveform(in_data):
                result = self.Rec.Result()
                sentence = self.CleanText(result)

                self.PublishToProcessing(self.MessageFactory.GetTextProcessingMessage(sentence, node))
                #self.PublishToProcessing(sentence)
        except Exception as a:
            print(a)
    
    def SubscribeToNodeAudio(self, node):
        """Process messages from the pubsub stream."""
        RedisPubSub = self.Redis.pubsub()
        RedisPubSub.subscribe(f"{node}:{SpeechToText_Channel}")
        for raw_message in RedisPubSub.listen():
            if raw_message["type"] != "message":
                continue
            self.ProcessRawAudio(raw_message, node)
            if self.IsListening:
                self.PlayAudio(raw_message, node)

    def CleanText(self, textToProcess):
        if textToProcess.find('{') < 0:
            return textToProcess;
        textObject = json.loads(textToProcess)
        text = textObject["text"]
        if len(text) > 0:
            print(text)
        return text.lower()
