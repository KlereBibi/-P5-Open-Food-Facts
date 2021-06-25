import mysql.connector
from manager import Manager
from category import Category
#from categoryproductmanager import CategoryProductManager

class CategoryManager(Manager):

    def save_catego_table(self, liste):

        """enregistre les catégories dans la base de donnée en appelant le constructeur de la classe mère"""

        sql = "INSERT INTO categories (id, name) VALUES (%s, %s) ON DUPLICATE KEY UPDATE name=name"
        
        value = liste

        self.cur.executemany(sql, value)

        self.connexion_off.commit()

        print(self.cur.rowcount, "ligne insérée.")

        self.cur.close()

        self.cur = self.connexion_off.cursor()

        """récupération des id des catégories en comparant avec la liste des catégories insérées"""

        liste_name_catego = []
        for element in liste:
            liste_name_catego.append(element[1])

        names = tuple(liste_name_catego)
        query= (
            "SELECT * FROM categories "
            f"WHERE name IN ({', '.join('%s' for _ in names)})" #comprends pas tout
        )
        self.cur.execute(query, names)
    
        res = self.cur.fetchall()

        liste_o_catego_id = []
        for element in res:
            liste_o_catego_id.append(Category(element[1], element[0]))

        return liste_o_catego_id

        
        
    

    
   