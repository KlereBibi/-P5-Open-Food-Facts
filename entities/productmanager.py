from category import Category
#from categorymanager import CategoryManager
import mysql.connector

class ProductManager:


    def change_tup(self,list):

        list_tup = []
        for element in list:
            list_tup.append((None, element.name, "a", element.nutriscore, "b"))
        
        return list_tup

    def save_product(self, list):
    
        list_tup_prod = self.change_tup(list)
        
        #connexion au base de données
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "184300",
            database = "off"
        )
        #créer un curseur de base de données pour effectuer des opérations SQL
        cur = db.cursor()

        sql = "INSERT INTO products (id, name, category, nutriscore, url) VALUES (%s, %s, %s, %s, %s)"

        value = list_tup_prod

        cur.executemany(sql, value)
        
        #valider la transaction
        db.commit()

        #afficher le nombre de lignes insérées
        print(cur.rowcount, "ligne insérée.")

        
# Hey, tu ma file une liste de prodiuits a enregistrer c'est cool :) par contre ces produits contiennent des categories mais pas d'ID ca veut dire qu'ils sont tout neuf
# Du coup je vais demander a mon pote categorie manager d'enregistrer ces categories en base d'abord et ensuite je vais enregistrer les produits