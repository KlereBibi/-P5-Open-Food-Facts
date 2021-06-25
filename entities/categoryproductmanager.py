from manager import Manager

class CategoryProductManager(Manager):

    def save_bond_cp_table(self, liste_bonde):
        
            """enregistre les catégories dans la base de donnée en appelant le constructeur de la classe mère"""

            sql = "INSERT INTO categories_products (id_products, id_categories) VALUES (%s, %s)"
            
            value = liste_bonde

            self.cur.executemany(sql, value)

            self.connexion_off.commit()

            print(self.cur.rowcount, "ligne insérée.")

            """récupération des id des catégories en comparant avec la liste des catégories insérées"""

       