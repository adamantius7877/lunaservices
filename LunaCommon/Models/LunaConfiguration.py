import json, uuid, copy
from typing import Dict
from Common import LUNA_CONFIG_FILE_PATH


class LunaConfiguration(object):

    def __init__(self):
        self.LoadedConfiguration = LunaConfig()
        self.LoadConfigurationFile(LUNA_CONFIG_FILE_PATH)

    def LoadConfiguration(self):
        self.LoadConfigurationFile(LUNA_CONFIG_FILE_PATH)

    def LoadConfigurationFile(self, path):
            f = open(path, "r")
            #jsonString = f.read()
            jsonContents = json.loads(f.read())
            #self.LoadedConfiguration.from_dict(jsonContents)
            
            self.LoadedConfiguration.NodeId = str(jsonContents['NodeId'])
            self.LoadedConfiguration.Name = str(jsonContents['Name'])
            for jsonQueue in jsonContents["RedisQueues"]:
                self.LoadedConfiguration.RedisQueues[jsonQueue["Name"]] = RedisQueue(jsonQueue["Name"], jsonQueue["Server"], jsonQueue["Port"], jsonQueue["Username"], jsonQueue["Password"], jsonQueue["ChannelName"])
            for jsonString in jsonContents["Neo4jConnectionStrings"]:
                conString = Neo4jConnectionString(jsonString)
                if conString.Name:
                    self.LoadedConfiguration.Neo4jConnectionStrings[conString.Name] = conString
            for jsonString in jsonContents["SqlLiteConnectionStrings"]:
                conString = SqlLiteConnectionString(jsonString)
                self.LoadedConfiguration.SqlLiteConnectionStrings[conString.Name] = conString

    def UpdateNeo4jConfiguration(self, dbInfo):
        try:
            db.set_connection(f"bolt://{dbInfo.Username}:{dbInfo.Password}@{dbInfo.Server}:{dbInfo.Port}")
        except Exception as ex:
            print(f'Unable to set neo4j connection: {ex}')

    def SaveConfiguration(self):
        self.SaveConfigurationFile(LUNA_CONFIG_FILE_PATH)

    def SaveConfigurationFile(self, path):
        try:
            json_object = self.LoadedConfiguration.to_json()
            with open(path, "w") as outfile:
                outfile.write(json_object)
        except KeyError as keyError:
            print(f'Unable to save configuration file due to a key error: {keyError}')
        except Exception as ex:
            print(f'Unable to save configuration file: {ex}')

    def SetupNeo4j(self, dbInfo):
        self.ConnectionString = f"bolt://{dbInfo.Username}:{dbInfo.Password}@{dbInfo.Server}:{dbInfo.Port}"
        db.set_connection(self.ConnectionString)



class LunaConfig:
    def __init__(self):
        self.RedisQueues: Dict[str,RedisQueue] = {}
        self.Neo4jConnectionStrings: Dict[str,Neo4jConnectionString] = {}
        self.SqlLiteConnectionStrings: Dict[str,SqlLiteConnectionString] = {}
        self.NodeId: str = '' 
        self.Name: str = '' 

    def to_dict(self):
        queues = []
        neo4jConnStrings = []
        sqlLiteConnStrings = []
        for key in self.RedisQueues:
            queues.append(self.RedisQueues[key].to_dict())
            print(self.RedisQueues[key].Name)
        for neo4jConnString in self.Neo4jConnectionStrings.values():
            neo4jConnStrings.append(neo4jConnString.to_dict())
        for sqlLiteConnString in self.SqlLiteConnectionStrings.values():
            sqlLiteConnStrings.append(sqlLiteConnString.to_dict())
        
        lunaConfigDict = {
            'RedisQueues': queues,
            'Neo4jConnectionStrings': neo4jConnStrings,
            'SqlLiteConnectionStrings': sqlLiteConnStrings,
            'NodeId': self.NodeId,
            'Name': self.Name,
        }
        return lunaConfigDict

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(self, config_dict):
        self.RedisQueues = [RedisQueue.from_dict(queue_dict) for queue_dict in config_dict.get("RedisQueues", {})]
        self.Neo4jConnectionStrings = [Neo4jConnectionString.from_dict(conn_dict) for conn_dict in config_dict.get("Neo4jConnectionStrings", {})]
        self.SqlLiteConnectionStrings = [SqlLiteConnectionString.from_dict(conn_dict) for conn_dict in config_dict.get("SqlLiteConnectionStrings", {})]
        self.NodeId = config_dict.get("NodeId", "")

    @classmethod
    def from_json(self, json_str):
        config_dict = json.loads(json_str)
        self.from_dict(config_dict)


class RedisQueue:
    def __init__(self):
        self.Name = ""
        self.Server = ""
        self.Port = ""
        self.Username = ""
        self.Password = ""
        self.ChannelName = ""

    def __init__(self, name="", server="", port="", username="", password="", channel_name=""):
        self.Name = name
        self.Server = server
        self.Port = port
        self.Username = username
        self.Password = password
        self.ChannelName = channel_name

    def to_dict(self) -> Dict[str,str]:
        return {
            "Name": self.Name,
            "Server": self.Server,
            "Port": self.Port,
            "Username": self.Username,
            "Password": self.Password,
            "ChannelName": self.ChannelName
        }

    @classmethod
    def from_dict(self, json_version: Dict[str,str]):
        self.Name = json_version["Name"]
        self.Server = json_version["Server"]
        self.Port = json_version["Port"]
        self.Username = json_version["Username"]
        self.Password = json_version["Password"]
        self.ChannelName = json_version["ChannelName"]


class Neo4jConnectionString:
    def __init__(self):
        self.Name = ""
        self.Server = ""
        self.Port = ""
        self.Username = ""
        self.Password = ""
        self.Database = ""

    def __init__(self, jsonDict: Dict[str,str]):
        self.from_dict(jsonDict)

    def to_dict(self) -> Dict[str,str]:
        return {
            "Name": self.Name,
            "Server": self.Server,
            "Port": self.Port,
            "Username": self.Username,
            "Password": self.Password,
            "Database": self.Database
        }

    @classmethod
    def from_dict(self, json_version: Dict[str,str]):
        self.Name = json_version["Name"]
        self.Server = json_version["Server"]
        self.Port = json_version["Port"]
        self.Username = json_version["Username"]
        self.Password = json_version["Password"]
        self.Database = json_version["Database"]


class SqlLiteConnectionString:
    def __init__(self):
        self.Name = ""
        self.Server = ""
        self.Port = ""
        self.Username = ""
        self.Password = ""
        self.Database = ""

    def __init__(self, jsonDict):
        self.from_dict(jsonDict)

    def to_dict(self) -> Dict[str,str]:
        return {
            "Name": self.Name,
            "Server": self.Server,
            "Port": self.Port,
            "Username": self.Username,
            "Password": self.Password,
            "Database": self.Database
        }

    @classmethod
    def from_dict(self, dict: Dict[str,str]):
        self.Name = dict["Name"]
        self.Server = dict["Server"]
        self.Port = dict["Port"]
        self.Username = dict["Username"]
        self.Password = dict["Password"]
        self.Database = dict["Database"]


