"""this module allows you to connectinteract with the database"""

import mysql.connector

class Manager:

    """parent class allowing connection to the database"""

    def __init__(self):
        
        """constructor containing the accesses to the database
        attri1 (def) :  open and store the connexion 
        attri2 (def) : creat the new cursor"""

        self.connexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "184300",
            database = "off"
        )
    
        self.cursor = self.connexion.cursor()

        

        