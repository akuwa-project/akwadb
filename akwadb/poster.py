__all__ = ['Poster']
from enum import Enum
from akwadb.annonce import TypeAnnonce
import uuid as uuid
import cv2

from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
url = "http://localhost:7474/db/data/"
username = "akwadb"
password = "akwadb"
gdb = GraphDatabase(url=url, username=username, password=password)

def createUiid():
    return str(uuid.uuid4())
# Chargement for picture
def importImageAndPath(p=[]):
    unique = createUiid()
    index = 0
    path = []
    while index<len(p):
        print(p[index])
        im = cv2.imread(p[index])
        mypath='/home/archange/PycharmProjects/akwadb/akwadb/photo/'+unique+p[index].split("/")[-1]
        mypath2='/home/archange/PycharmProjects/akwadb/akwadb/photo/'+unique+p[index].split("/")[-1]
        path.append(mypath2)
        cv2.imwrite(mypath, im)
        index =index+1
    return path

def imagePath(p=[]):
    path = []
    index = 0
    while index<len(p):
        mypath='/home/archange/PycharmProjects/akwadb/akwadb/photo/'+p[index].split("/")[-1]
        path.append(mypath)
        index =index+1
    return path

class EtatPoste(Enum):
    Payer = 1
    Louer = 2
    Retirer = 3

class Poster():
    photo= []
    information =  []

    # create a poste
    def addNoed_Poste(self,id,titre,photo,montant,date,adresse,commentaire,etatPoste,information,typeAnnonce):
        photopath=importImageAndPath(photo)
        myPoste = gdb.nodes.create(id=id,titre=titre,photo=photopath,montant=montant,date=date,adresse=adresse,
                        commentaire=commentaire,etatPoste=etatPoste,information=information,typeAnnonce=typeAnnonce)
        poster = gdb.labels.create("Poste")
        poster.add(myPoste)

    #Update a poste node
    def updatePoste(self,annonce_id,etatPoste):
        query="MATCH (n:Poste { id:"+"'"+annonce_id+"'"+"}) SET n.etatPoste="+"'"+etatPoste+"'"
        gdb.query(query, returns=(client.Node, "unicode", client.Relationship))


    #Update a poste node
    def deletePoste(self,annonce_id):
        query="MATCH (n:Poste { id:"+"'"+annonce_id+"'"+"}) DETACH DELETE n"
        gdb.query(query)


    # Create a relationship with poste and annonce.
    def add_relation_poste_user(self,user_name,id):
        query="MATCH (a:E_user),(b:Poste) WHERE a.user_name = "+"'"+user_name+"'"+" AND b.id = "+"'"+ id+"'"+" CREATE (a)-[r:ToPost]->(b) RETURN r"
        gdb.query(query)



    # def recupernod(self,label,labelText):
    #     Q(label, exact=labelText)
    #     results = gdb.nodes.filter(lookup)
    #     return results[0]


    # get a E_user by criteria
    def getAllPostOfEuser(self,user_name):
        tableOfUser = []

        query="MATCH (a:E_user)-[:ToPost]->(b:Poste) WHERE a.user_name = "+"'"+user_name+"'"+ "RETURN b"
        results = gdb.query(query, returns=(client.Node, "unicode", client.Relationship))
        for element in results:
            x=str(element).split("/")[-1].split(">")[0]
            n = gdb.nodes.get(x)
            tableOfUser.append(n.properties)
        return tableOfUser


if __name__ == "__main__":
    b = Poster()
    # node_id= str(uuid.uuid4())
    # b.addNoed_Poste(node_id,"Maison",["/home/archange/Images/Capture d’écran de 2019-06-06 10-55-54.png",
    #                                        "/home/archange/Images/dev_Incremental_Iteratif.png"],"25000","22-02-2019","Cotonou","Villa propre",EtatPoste.Payer.name,["a","d","m"],TypeAnnonce.Location.name)

    # b.add_relation_poste_user("qosyx2",node_id)
    # b.updatePoste(node_id,"Reussi")
    # b.deletePoste("a446c1b2-4fab-4a84-8e17-737f97fe3f2f")
    l=b.getAllPostOfEuser("qosyx2")
    print(l)
