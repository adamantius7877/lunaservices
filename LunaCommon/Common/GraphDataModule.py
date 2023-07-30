from neo4j import GraphDatabase

class GraphDataModule(object):

    Driver = []
    def __init__(self, dbInfo):
        self.ConnectionString = f"neo4j://{dbInfo.Server}:{dbInfo.Port}"
        GraphDataModule.Driver = GraphDatabase.driver(self.ConnectionString, auth=(dbInfo.Username, dbInfo.Password))
