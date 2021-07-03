from manager import Manager

class StoreProductManager(Manager):

    def save_bond_sp_table(self, liste_bonde):
        
            """enregistre les catégories dans la base de donnée en appelant le constructeur de la classe mère"""

            sql = "INSERT INTO stores_products (id_products, id_stores) VALUES (%s, %s)"
            
            value = liste_bonde

            self.cur.executemany(sql, value)

            self.connexion_off.commit()

            print(self.cur.rowcount, "ligne insérée.")
