import mysql.connector
from models.managers.manager import Manager
from models.entities.brand import Brand


class BrandManager(Manager):
    
    def save_brand_database(self, liste_tup_o_brand):

        """enregistre les catégories dans la base de donnée en appelant le constructeur de la classe mère"""

        sql = "INSERT INTO brands (id, name) VALUES (%s, %s) ON DUPLICATE KEY UPDATE name=name"
        
        value = liste_tup_o_brand

        self.cursor.executemany(sql, value)

        self.connexion_database_off.commit()

        print(self.cursor.rowcount, "ligne insérée.")

        self.cursor.close()

        self.cursor = self.connexion_database_off.cursor()


        liste_name_brands = []
        for element in liste_tup_o_brand:
            liste_name_brands.append(element[1])

        names = tuple(liste_name_brands)
        query= (
            "SELECT * FROM brands "
            f"WHERE name IN ({', '.join('%s' for _ in names)})" 
        )
        self.cursor.execute(query, names)
    
        brands_id_name = self.cursor.fetchall()

        liste_tup_o_brand_id = []
        for element in brands_id_name:
             liste_tup_o_brand_id.append(Brand(element[1], element[0]))

        return  liste_tup_o_brand_id
