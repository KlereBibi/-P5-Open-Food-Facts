import mysql.connector
from manager import Manager
from categoryproductmanager import CategoryProductManager

class CategoryManager(Manager):

    def save_catego_table(self, liste):

        """enregistre les catégories dans la base de donnée en appelant le constructeur de la classe mère"""

        sql = "INSERT INTO categories (id, name) VALUES (%s, %s) ON DUPLICATE KEY UPDATE name=name"
        
        value = liste

        self.cur.executemany(sql, value)

        self.connexion_off.commit()

        print(self.cur.rowcount, "ligne insérée.")

        """récupération des id des catégories en comparant avec la liste des catégories insérées"""

        liste_name_catego = []
        for element in liste:
            liste_name_catego.append(element[1])

        t = tuple(liste_name_catego)
        query= "SELECT * FROM categories WHERE name IN {}".format(t)

        self.cur.execute(query)
    
        res = self.cur.fetchall()
        
        print(res)

        #afficher le nombre de lignes insérées
        

        
    

    
   