import mysql.connector
from models.managers.manager import Manager

class CategoryProductManager(Manager):

    def save_categoryproduct_database(self, liste_tupe_id_categoryproduct):
        
            """enregistre les catégories dans la base de donnée en appelant le constructeur de la classe mère"""

            sql = "INSERT INTO categories_products (id_products, id_categories) VALUES (%s, %s)"
            
            value = liste_tupe_id_categoryproduct

            self.cursor.executemany(sql, value)

            self.connexion_database_off.commit()

            print(self.cursor.rowcount, "ligne insérée.")

            """récupération des id des catégories en comparant avec la liste des catégories insérées"""

       