import mysql.connector
from constante import REGISTERCATEGORIES
from constante import REGISTERPRODUCT

class ConnexionOff:

        
    def save_table(self, constante, element):

    #connexion au base de données
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "184300",
            database = "off"
        )
    
        cur = db.cursor()

        sql = constante
        
        value = element

        cur.executemany(sql, value)

        db.commit()

        #afficher le nombre de lignes insérées
        print(cur.rowcount, "ligne insérée.")


       