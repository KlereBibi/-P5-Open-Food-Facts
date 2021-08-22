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
        #self.connexion.reconnect()
        #self.cursor = self.connexion.cursor()

    def read_command_sql(self, read_file):

        """method allowing to read sql files and to execute them in the database
        Arg:
        file : file to read"""

        file = join(dirname(dirname(abspath(__file__))), "settings", read_file)

        with open(file) as infile:
            sqlrequests = infile.read().split(';')
            for line in sqlrequests:
                if line.strip():
                    cursor = self.connexion.cursor()
                    cursor.execute(line)
                    self.end_request(cursor)

    def end_request(self, cursor):

        self.connexion.commit()
        cursor.close()
        
        
        
    

        
