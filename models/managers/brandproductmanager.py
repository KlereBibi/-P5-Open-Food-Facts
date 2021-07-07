from models.managers.manager import Manager

class BrandProductManager(Manager):

    def save_brandpoduct_database(self, liste_bonde_id_brand):
        
            """enregistre les catégories dans la base de donnée en appelant le constructeur de la classe mère"""

            sql = "INSERT INTO brands_products (id_products, id_brands) VALUES (%s, %s)"
            
            value = liste_bonde_id_brand

            self.cursor.executemany(sql, value)

            self.connexion_database_off.commit()

            print(self.cursor.rowcount, "ligne insérée.")

            

       