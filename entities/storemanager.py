import mysql.connector
from manager import Manager
from store import Store

class StoreManager(Manager):
    
    def save_store_table(self, liste):

        """enregistre les catégories dans la base de donnée en appelant le constructeur de la classe mère"""

        sql = "INSERT INTO stores (id, name) VALUES (%s, %s) ON DUPLICATE KEY UPDATE name=name"
        
        value = liste

        self.cur.executemany(sql, value)

        self.connexion_off.commit()

        print(self.cur.rowcount, "ligne insérée.")

        self.cur.close()

        self.cur = self.connexion_off.cursor()


        liste_name_store = []
        for element in liste:
            liste_name_store.append(element[1])

        names = tuple(liste_name_store)
        query= (
            "SELECT * FROM stores "
            f"WHERE name IN ({', '.join('%s' for _ in names)})" #comprends pas tout
        )
        self.cur.execute(query, names)
    
        res = self.cur.fetchall()

        liste_o_stores_id = []
        for element in res:
            liste_o_stores_id.append(Store(element[1], element[0]))

        return liste_o_stores_id
