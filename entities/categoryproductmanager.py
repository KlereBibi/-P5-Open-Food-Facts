from manager import Manager

class CategoryProductManager(Manager):

    def take_id_product(self):
        
        super().__init__()

        self.cur.execute("SELECT id, name FROM products")

        res = self.cur.fetchall()

        return res

    def take_id_catego(self):
    
        super().__init__()

        self.cur.execute("SELECT * FROM categories")

        res = self.cur.fetchall()

        return res

    def save_liaison(self, liste_id):

        
        super().__init__() #constructeur de la class mère
        
        sql = "INSERT INTO categories_products (id_products, id_categories) VALUES (%s, %s)"

        value = liste_id

        self.cur.executemany(sql, value)

        self.connexion_off.commit()
        
        #afficher le nombre de lignes insérées
        print(self.cur.rowcount, "ligne insérée.")

        
    
