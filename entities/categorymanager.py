import mysql.connector
from connexion import ConnexionOff
from constante import REGISTERCATEGORIES

class CategoryManager:
    
    def __init__(self):

        self.call_connexion = ConnexionOff()
    
        self.list_tup_catego = []

    # def printlist(self):
    #     print(self.list_tup_catego)

    def save_catego_table(self):

        connex = ConnexionOff()
        connex.save_table(REGISTERCATEGORIES, self.list_tup_catego)
        
        

        