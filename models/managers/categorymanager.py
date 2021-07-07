import mysql.connector
from models.managers.manager import Manager
from models.entities.category import Category


class CategoryManager(Manager):

    def save_categories_database(self, liste_tup_categories):

        """enregistre les catégories dans la base de donnée en appelant le constructeur de la classe mère"""

        sql = "INSERT INTO categories (id, name) VALUES (%s, %s) ON DUPLICATE KEY UPDATE name=name"
        
        value = liste_tup_categories

        self.cursor.executemany(sql, value)

        self.connexion_database_off.commit()

        print(self.cursor.rowcount, "ligne insérée.")

        self.cursor.close()

        self.cursor = self.connexion_database_off.cursor()

        """récupération des id des catégories en comparant avec la liste des catégories insérées"""

        liste_name_categories = []
        for element in liste_tup_categories:
            liste_name_categories.append(element[1])

        names = tuple(liste_name_categories)
        query= (
            "SELECT * FROM categories "
            f"WHERE name IN ({', '.join('%s' for _ in names)})" 
        )
        self.cursor.execute(query, names)
    
        categories_id_name = self.cursor.fetchall()

        liste_o_catego_id = []
        for element in categories_id_name:
            liste_o_catego_id.append(Category(element[1], element[0]))

        return liste_o_catego_id

        
        
    

    
   