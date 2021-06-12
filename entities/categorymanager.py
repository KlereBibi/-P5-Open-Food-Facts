import mysql.connector
from manager import Manager
from categoryproductmanager import CategoryProductManager

class CategoryManager(Manager):

    def save_catego_table(self, liste):

        """méthode enregistrant les catégories dans la base de donnée en appelant le constructeur de la classe mère"""

        super().__init__()
       
        sql = "INSERT IGNORE INTO categories (id, name) VALUES (%s, %s)"
        
        value = liste

        self.cur.executemany(sql, value)

        self.connexion_off.commit()

         #afficher le nombre de lignes insérées
        print(self.cur.rowcount, "ligne insérée.")

    
   