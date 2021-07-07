import mysql.connector

class Manager:

    """classe mère des managers possédants les propriété de connexion à la base de donnée"""

    def __init__(self):

        """constructeur de la classe avec les attributs de connexion à la base de donnée off & création du curseur"""

        self.connexion_database_off = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "184300",
            database = "off"
        )
    
        self.cursor = self.connexion_database_off.cursor()

        

        