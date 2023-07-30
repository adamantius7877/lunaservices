from Models import Data

class LunaNodeRegistrationModule(object):
    """This class is used to listen to audio sources and interpet them into text"""

    def __init__(self, lunaNode):
        self.Luna = lunaNode

    def Register(self):
        data = Data()
        data.NodeId = self.Luna.NodeId
        data.Ip = self.Luna.GetIp()
        data.Name = self.Luna.GetHostName()
        self.Luna.PublishToRegistration(self.Luna.MessageFactory.GetRegistrationMessage(data, self.Luna.NodeId))

    def NodeRegisterResponse(self, rawmessage):
        message = self.Luna.GetMessage(rawmessage)
        if message.Data["IsSuccessful"]:
            if message.Data["NodeId"] != self.Luna.NodeId:
                print(f'MessageData: {message.Data["NodeId"]}')
                self.Luna.SetNodeId(message.Data["NodeId"])
            self.Luna.Speak(self.Luna.GetGreeting())
            self.Luna.Configuration.SaveConfiguration()
            print(f"Registered: {self.Luna.NodeId}")
            self.Luna.ListenModule.Listen()
        else:
            self.Luna.Speak("Unable to connect")

