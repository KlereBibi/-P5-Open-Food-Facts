"""this module allows you to connectinteract with the database"""

import mysql.connector

class Manager:

    """parent class allowing connection to the database"""

    def __init__(self):
        
        """constructor containing the accesses to the database"""
      
        self.connexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "184300",
            database = "off"
        )
    
        self.cursor = self.connexion.cursor()

    def read_command_sql(self, file):

        """method allowing to read sql files and to execute them in the database
        Arg: 
        file : file to read"""

        self.cursor = self.connexion.cursor()

        database = join(dirname(dirname(abspath(__file__))), "settings", file)
        print(database)
        with open(database) as infile:
            sqlrequests = infile.read().split(';')
            for sqlrequests in sqlrequests:
                if sqlrequests.strip():
                    self.cursor.execute(sqlrequests)

        

        