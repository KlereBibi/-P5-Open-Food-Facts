import mysql.connector

class CategoryManager:
    
    def __init__(self):

        self.list_tup_catego = []
    

    def save_catego_tup(self, element):

        self.list_tup_catego.append((None, element.name))

    def save_catego_table(self):

        
        #connexion au base de données
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "184300",
            database = "off"
        )
        #créer un curseur de base de données pour effectuer des opérations SQL
        cur = db.cursor()

        #requéte SQL
        sql = "INSERT IGNORE INTO categories (id, name) VALUES (%s, %s)"
        #les valeurs de la requéte SQL
        value = self.list_tup_catego
        #exécuter le curseur avec la méthode execute() et transmis la requéte SQL
        cur.executemany(sql, value)
        #valider la transaction
        db.commit()
        #afficher le nombre de lignes insérées
    
        print(cur.rowcount, "ligne insérée.")

        