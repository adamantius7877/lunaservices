from Common.enums import ServiceEnums
from Models import BaseService, Data
from Models.Neo4j.LunaNode import LunaNode
from Messages import DataMessages

class RegistrationService(BaseService.BaseService):
    
    def __init__(self):
        super().__init__(ServiceEnums.ServiceType.Registration)
        self.SubscribeToRegistration(self.RegisterNode)
        self.StartRedis()

    def RegisterNode(self, rawmessage):
        message = self.GetMessage(rawmessage)
        existingNode: LunaNode = LunaNode()
        try:
            existingNode.GetWithNodeId(message.Data["NodeId"])
            if existingNode.NodeId is None or existingNode.NodeId == "":
                print(f'NodeId not found: {message.Data["NodeId"]} (from try)')
        except:
            print(f'NodeId not found: {message.Data["NodeId"]}')
            existingNode = None

        if existingNode is None:
            try:
                existingNode = LunaNode.nodes.first_or_none(Ip=message.Data["Ip"])
                if existingNode.NodeId is None or existingNode.NodeId == "":
                    print(f'Node Ip not found: {message.Data["Ip"]} (from try)')
            except:
                print(f'Node Ip not found: {message.Data["Ip"]}')
                existingNode = None

        if existingNode is None:
            try:
                existingNode = LunaNode.nodes.first_or_none(Name=message.Data["Name"])
                if existingNode.NodeId is None or existingNode.NodeId == "":
                    print(f'Node Hostname not found: {message.Data["Name"]} (from try)')
            except:
                print(f'Node Hostname not found: {message.Data["Name"]}')
                existingNode = None

        node = LunaNode()
        if existingNode is None or existingNode.NodeId is None or existingNode.NodeId == "":
            node = LunaNode()
            node.Name = message.Data["Name"]
            node.Ip = message.Data["Ip"]
            node.NodeId = message.Data["NodeId"]
            node.Add()
        else:
            node = existingNode

        # Add to speechtotext service
        self.PublishToSpeechToText(self.MessageFactory.GetSpeechToTextMessage(node.NodeId, node.NodeId))

        data = Data()
        data.Name = node.Name
        data.Ip = node.Ip
        data.NodeId = node.NodeId
        data.IsSuccessful = True
        registrationMessage = self.MessageFactory.GetRegistrationMessage(data, message.NodeId)
        self.PublishToNodeRegistration(registrationMessage)
