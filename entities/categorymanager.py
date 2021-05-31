import mysql.connector

class CategoryManager:


    def save_into_table(self, element):

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
        sql = "INSERT INTO categories (id, name) VALUES (%s, %s)"
        #les valeurs de la requéte SQL
        value = (None, element)
        #exécuter le curseur avec la méthode execute() et transmis la requéte SQL
        cur.execute(sql, value)
        #valider la transaction
        db.commit()
        #afficher le nombre de lignes insérées
      
        print(cur.rowcount, "ligne insérée.")