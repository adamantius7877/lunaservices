from Common.enums import MessageType, MessageSubType, ServiceType, DataType
from Models import BaseService
from Models.Neo4j import LunaNode, LunaBlueprint, LunaCapability, LunaDevice, LunaGroup, LunaProperty, LunaRoom, LunaUser, LunaZone, LunaKeyword, LunaDirective, LunaItem

class StorageService(BaseService.BaseService):

    def __init__(self):
        super().__init__(ServiceType.Storage)
        self.SubscribeToStorage(self.ProcessMessage)
        self.StartRedis()

    def ProcessMessage(self, rawmessage):
        message = self.GetMessage(rawmessage)
        if message.MessageType == MessageType.Import:
            self.ImportData(message)

    def ImportData(self, message):
        # Determine the type of data to import
        if message.Data.DataType == DataType.Blueprint:
            self.ImportBlueprints(message)
        elif message.Data.DataType == DataType.Capability:
            self.ImportCapabilities(message)
        elif message.Data.DataType == DataType.Device:
            self.ImportDevices(message)
        elif message.Data.DataType == DataType.Directive:
            self.ImportDirectives(message)
        elif message.Data.DataType == DataType.Group:
            self.ImportGroups(message)
        elif message.Data.DataType == DataType.Item:
            self.ImportItems(message)
        elif message.Data.DataType == DataType.Keyword:
            self.ImportKeywords(message)
        elif message.Data.DataType == DataType.Node:
            self.ImportNodes(message)
        elif message.Data.DataType == DataType.Property:
            self.ImportProperties(message)
        elif message.Data.DataType == DataType.Room:
            self.ImportRooms(message)
        elif message.Data.DataType == DataType.User:
            self.ImportUsers(message)
        elif message.Data.DataType == DataType.Zone:
            self.ImportZones(message)

    def ImportBlueprints(self, message):
        for rawblueprint in message.Data.DataToImport:
            blueprint = LunaBlueprint()
            blueprint.Populate(rawblueprint)
            blueprint.Add()

    def ImportZones(self, message):
        for rawzone in message.Data.DataToImport:
            zone = LunaZone()
            zone.Populate(rawzone)
            zone.Add()
            
    def ImportUsers(self, message):
        for rawuser in message.Data.DataToImport:
            user = LunaUser()
            user.Populate(rawuser)
            user.Add()

    def ImportCapabilities(self, message):
        for rawdata in message.Data.DataToImport:
            capability = LunaCapability()
            fromNodeName = rawdata[0]
            toNodeName = rawdata[2]
            fromNode = LunaKeyword()
            fromNode.Get(fromNodeName)
            toNode = LunaKeyword()
            toNode.Get(toNodeName)
            fromNode.AddRelationship(capability, toNode)


    def ImportDevices(self, message):
        for rawdevice in message.Data.DataToImport:
            device = LunaDevice()
            device.Populate(rawdevice)
            device.Add()

    def ImportDirectives(self, message):
        for rawdata in message.Data.DataToImport:
            directive = LunaDirective()
            fromNodeName = rawdata[0]
            toNodeName = rawdata[2]
            fromNode = LunaKeyword()
            fromNode.Get(fromNodeName)
            toNode = LunaKeyword()
            toNode.Get(toNodeName)
            fromNode.AddRelationship(directive, toNode)

    def ImportGroups(self, message):
        for rawgroup in message.Data.DataToImport:
            group = LunaGroup()
            group.Populate(rawgroup)
            group.Add()

    def ImportItems(self, message):
        for rawdata in message.Data.DataToImport:
            item = LunaItem()
            fromNodeName = rawdata[0]
            toNodeName = rawdata[2]
            fromNode = LunaKeyword()
            fromNode.Get(fromNodeName)
            toNode = LunaKeyword()
            toNode.Get(toNodeName)
            fromNode.AddRelationship(item, toNode)

    def ImportKeywords(self, message):
        for rawkeyword in message.Data.DataToImport:
            keyword = LunaKeyword()
            keyword.Populate(rawkeyword)
            keyword.Add()

    def ImportNodes(self, message):
        for rawnode in message.Data.DataToImport:
            node = LunaNode()
            node.Populate(rawnode)
            node.Add()

    def ImportProperties(self, message):
        for rawproperty in message.Data.DataToImport:
            lunaproperty = LunaProperty()
            lunaproperty.Populate(rawproperty)
            lunaproperty.Add()

    def ImportRooms(self, message):
        for rawroom in message.Data.DataToImport:
            room = LunaRoom()
            room.Populate(rawroom)
            room.Add()
