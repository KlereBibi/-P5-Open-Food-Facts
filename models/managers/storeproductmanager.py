from models.managers.manager import Manager

class StoreProductManager(Manager):

    def save_storeproduct_database(self, liste_tup_store):
        
            """enregistre les catégories dans la base de donnée en appelant le constructeur de la classe mère"""

            sql = "INSERT INTO stores_products (id_products, id_stores) VALUES (%s, %s)"
            
            value = liste_tup_store

            self.cursor.executemany(sql, value)

            self.connexion_database_off.commit()

            print(self.cursor.rowcount, "ligne insérée.")
