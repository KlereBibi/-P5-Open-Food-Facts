"""this module allows you to connectinteract with the database"""

from mysql import connector
from os.path import join, dirname, abspath


class Manager:

    """parent class allowing connection to the database"""

    def __init__(self):

        """constructor containing the accesses to the database"""

        self.connexion = connector.connect(
            host="localhost",
            user="root",
            password="184300",
            database="off",
            use_unicode=True,
            charset='utf8mb4'
        )

        self.cursor = self.connexion.cursor()

    def read_command_sql(self, file):

        """method allowing to read sql files and to execute them in the database
        Arg:
        file : file to read"""

        database = join(dirname(dirname(abspath(__file__))), "settings", file)

        with open(database) as infile:
            sqlrequests = infile.read().split(';')
        
        self.whrite_database(sqlrequests)

        infile.close
    
    def whrite_database(self, sqlrequests):

        for line in sqlrequests:
            if line.strip():
                cursor = self.connexion.cursor()
                cursor.execute(line)
                cursor.close()
                
        
    

        
