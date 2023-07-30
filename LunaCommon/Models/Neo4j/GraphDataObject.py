from Common import GraphDataModule
import json

class GraphDataObject(object):

    def __init__(self, typeName):
        self.Driver = GraphDataModule.Driver
        self.TypeName = typeName 
        self.Name = ""
        self.Id = 0

    def GetProps(self):
        props = []
        [props.append(a) for a in dir(self) if not a.startswith('__') and not a.startswith('Driver') and not callable(getattr(self, a))]
        return props

    def GetDict(self):
        dictReturn = {}
        props = self.GetProps()
        for prop in props:
            dictReturn[prop] = getattr(self, prop)
        return dictReturn

    def GetMap(self):
        mapping = "{"
        props = self.GetDict()
        for key in props:
            if isinstance(props[key], str):
                mapping += f"{key}:'{props[key]}',"
            else:
                mapping += f"{key}:{props[key]},"
        mapping = mapping[0:len(mapping)-1]
        mapping += "}"
        return mapping

    def Update(self):
        with self.Driver.session() as session:
            session.execute_write(self.UpdateTx)

    def Add(self):
        with self.Driver.session() as session:
            session.execute_write(self.AddTx)

    def AddTx(self, tx):
        mapping = self.GetMap()
        query = f"CREATE ({self.Name}:{self.TypeName} {mapping})"
        tx.run(query)

    def UpdateTx(self, tx):
        query = f"MATCH ({self.Name}:{self.TypeName})"
        mapping = self.GetMap()
        query += f"{self.Name} = {mapping}"
        tx.run(query)

    def Serialize(self):
        return json.dumps(self.GetDict())

    def Deserialize(self, rawstring):
        jsonObject = json.loads(rawstring)
        props = self.GetProps()
        for prop in props:
            if not isinstance(getattr(self, prop), type([])):
                setattr(self, prop, jsonObject[f"n.{prop}"])

    def RelationshipQuery(self):
        pass

    def Populate(self, record):
        props = self.GetProps()
        for prop in props:
            if not isinstance(getattr(self, prop), type([])):
                propValue = ''
                try:
                    propValue = record[f"{prop}"]
                except:
                    propValue = ''
                setattr(self, prop, propValue)

class GraphNode(GraphDataObject):

    def __init__(self, typeName):
        super().__init__(typeName)

    def AddRelationship(self, relationship, toNode):
        with self.Driver.session() as session:
            session.execute_write(self.AddRelationshipTx, relationship, toNode)

    def AddRelationshipTx(self, tx, relationship, toNode):
        query = "MERGE $selfnode$relations$tonode"
        tx.run(query, selfnode = self.RelationshipQuery(), relations=relationship.RelationshipQuery(), tonode = toNode.RelationshipQuery())

    def RelationshipQuery(self):
        return f"({self.Name}:{self.TypeName})"

    def Get(self, name):
        with self.Driver.session() as session:
            session.execute_read(self.GetTx, name)

    def GetTx(self, tx, name):
        query = f"MATCH (n:{self.TypeName}) WHERE n.Name = $name RETURN n"
        for record in tx.run(query, name=name):
            self.Populate(record)

    def GetAll(self):
        with self.Driver.session() as session:
            return session.execute_read(self.GetAllTx)

    def GetAllTx(self, tx):
        query = f"MATCH (n:{self.TypeName})"
        nodes = []
        for record in tx.run(query):
            newNode = self.GetNew()
            newNode.Populate(record)
            nodes.append(newNode)
        return nodes

    def GetNew(self):
        return  self.__class__()


class GraphRelationship(GraphDataObject):

    def __init__(self, typeName):
        super().__init__(typeName)

    def RelationshipQuery(self):
        return f"-[{self.Name}:{self.TypeName}]->"
