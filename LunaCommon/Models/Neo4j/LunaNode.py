from .GraphDataObject import GraphNode
from Common.enums import GraphNodeType

# nodes are contained in rooms and have associated devices they can use or communicate with
class LunaNode(GraphNode):

    def __init__(self):
        super().__init__("LunaNode")
        self.NodeId = "" 
        self.Name = ""
        self.Ip = ""
        self.Hostname = ""
        self.Room = []
        self.Devices = []

    def GetWithNodeId(self, name):
        with self.Driver.session() as session:
            session.execute_read(self.GetWithNodeIdTx, name)

    def GetWithNodeIdTx(self, tx, nodeId):
        query = f"MATCH (n:{self.TypeName}) WHERE n.NodeId = $nodeId RETURN n"
        for record in tx.run(query, nodeId=nodeId):
            self.Populate(record)
