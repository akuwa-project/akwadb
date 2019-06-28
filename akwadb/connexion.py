__all__ = ['Connect']
from neo4jrestclient.client import GraphDatabase

class Connect():
    url = "http://localhost:7474/db/data/"
    username = "akwadb"
    password = "akwadb"
    def connexion(self):
        gdb = GraphDatabase(url=self.url, username=self.username, password=self.password)
        return gdb