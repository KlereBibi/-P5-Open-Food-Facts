from category import Category
from categorymanager import CategoryManager
import mysql.connector

class ProductManager:


    def save_product(self, list):
        
        #aobjet categorie manager appelé 
        categomanager = CategoryManager()

        #creation de liste de tuple
        list_tup_prod = []

        #transformation en tuples
        for element in list: 
            list_tup_prod.append((None, element.name, element.nutriscore, element.url))
            for catego in element.categories:
                categomanager.save_catego_tup(catego)

        categomanager.save_catego_table()

        #connexion au base de données
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "184300",
            database = "off"
        )
        #créer un curseur de base de données pour effectuer des opérations SQL
        cur = db.cursor()

        sql = "INSERT INTO products (id, name, nutriscore, url) VALUES (%s, %s, %s, %s)"

        value = list_tup_prod

        cur.executemany(sql, value)
        
        #valider la transaction
        db.commit()

        #afficher le nombre de lignes insérées
        print(cur.rowcount, "ligne insérée.")

 