__all__ = ['E_user']
from akwadb.typeEUser import TypeEUser
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

url = "http://localhost:7474/db/data/"
username = "akwadb"
password = "akwadb"
gdb = GraphDatabase(url=url, username=username, password=password)

class E_user():
    # Create a E_user
    def addNoed_User(self,nom,prenom,mail,tel,user_name,categorie):
        myUser = gdb.nodes.create(name=nom,prenom=prenom,mail=mail,tel=tel,user_name=user_name,categorie=categorie)
        e_user = gdb.labels.create("E_user")
        e_user.add(myUser)

    # Create all E_user
    def getAllEUser(self):
        tableOfUser = []
        myUser = gdb.labels.get("E_user")
        p= myUser.all()
        # print(len(p))
        for element in p:
            x=str(element).split("/")[-1].split(">")[0]
            n = gdb.nodes.get(x)
            tableOfUser.append(n.properties)
        return tableOfUser

    # get a E_user by criteria
    def getEUserByCriteria(self,query):
        tableOfUser = []
        results = gdb.query(query, returns=(client.Node, "unicode", client.Relationship))
        for element in results:
            x=str(element).split("/")[-1].split(">")[0]
            n = gdb.nodes.get(x)
            tableOfUser.append(n.properties)
        return tableOfUser



if __name__ == "__main__":
    b = E_user()
    # type_euser=TypeCategorie.Particulier.name
    # print(type_euser)
    b.addNoed_User("GANDONOU", "Jean-Baptiste", "archange.jb@gmail.com","97845152", "qosyx",TypeEUser.Particulier.name)
    # b.addNoed_User("GANDONOU1", "Jean-Baptiste", "archange.jb@gmail.com","97845152", "qosyx2",TypeEUser.Particulier.name)
    k=b.getEUserByCriteria("MATCH (n) RETURN n")
    print(k)
