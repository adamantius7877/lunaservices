import datetime, json

class LunaMessage(object):
    '''This is an abstract base class for all other messages to use'''

    def __init__(self):
        self.NodeId = ""
        self.MessageType = []
        self.TimeStamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.Data = []

        
    def FromJson(self, jsonMessage):
        self.NodeId = jsonMessage["NodeId"]
        self.MessageType = jsonMessage["MessageType"]
        self.TimeStamp = str(jsonMessage["TimeStamp"])
        self.Data = jsonMessage["Data"]

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
