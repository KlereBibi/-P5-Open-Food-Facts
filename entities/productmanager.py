from category import Category
from categorymanager import CategoryManager
import mysql.connector

class ProductManager:

    def take_product_list(self, list):

        """méthode permettant de récupérer la liste de produit appeler dans API manager, retournant la liste de produit pour Product Manager """
        return list
    
    def data_cate(self, list):

        """méthode permettant d'accéder aux objets catégories de chaque produits pour ensuite appeler category manager qui enregistrera les produits dans la table"""

        for element in self.take_product_list(list):
            for each in element.categories:
                if each.id == None:
                    categomana = CategoryManager()
                    categomana.save_into_table(each.name)

        #self.save_product(list)

    def save_product(self, list):

        for element in self.take_product_list(list):

            if element.id == None : 
                
                #connexion au base de données
                db = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "184300",
                    database = "off"
                )
                #créer un curseur de base de données pour effectuer des opérations SQL
                cur = db.cursor()

                #requéte SQL
                sql = "INSERT INTO products (id, name, categories, nutriscore, url) VALUES (%s, %s, %s, %s, %s)"
                #les valeurs de la requéte SQL
                value = (None, element.name, a, element.nutriscore, None)
                #exécuter le curseur avec la méthode execute() et transmis la requéte SQL
                cur.execute(sql, value)
                #valider la transaction
                db.commit()

                
                #afficher le nombre de lignes insérées
                
                print(cur.rowcount, "ligne insérée.")

        
# Hey, tu ma file une liste de prodiuits a enregistrer c'est cool :) par contre ces produits contiennent des categories mais pas d'ID ca veut dire qu'ils sont tout neuf
# Du coup je vais demander a mon pote categorie manager d'enregistrer ces categories en base d'abord et ensuite je vais enregistrer les produits