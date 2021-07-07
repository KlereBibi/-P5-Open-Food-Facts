import mysql.connector
from models.managers.manager import Manager
from models.entities.store import Store

class StoreManager(Manager):
    
    def save_store_database(self, liste_tup_o_store):

        """enregistre les catégories dans la base de donnée en appelant le constructeur de la classe mère"""

        sql = "INSERT INTO stores (id, name) VALUES (%s, %s) ON DUPLICATE KEY UPDATE name=name"
        
        value = liste_tup_o_store

        self.cursor.executemany(sql, value)

        self.connexion_database_off.commit()

        print(self.cursor.rowcount, "ligne insérée.")

        self.cursor.close()

        self.cursor = self.connexion_database_off.cursor()


        liste_name_store = []
        for element in liste_tup_o_store:
            liste_name_store.append(element[1])

        names = tuple(liste_name_store)
        query= (
            "SELECT * FROM stores "
            f"WHERE name IN ({', '.join('%s' for _ in names)})" #comprends pas tout
        )
        self.cursor.execute(query, names)
    
        store_id_name = self.cursor.fetchall()

        liste_o_stores_id = []
        for element in store_id_name :
            liste_o_stores_id.append(Store(element[1], element[0]))

        return liste_o_stores_id
