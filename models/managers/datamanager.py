
"""module to delete and creat tables in database """

from models.managers.manager import Manager
from os.path import join, dirname, abspath

class DataManager(Manager):

    """class to communicate with table brandsproducts
        Args:
        -Manager (class parent): initializes the connection to the database """

    def delete_tables(self):

        """method to delete table in database """
        
        self.cursor = self.connexion.cursor()

        command = join(dirname(dirname(abspath(__file__))), "settings", "deletetables.sql")
        with open(command) as infile:
            sqlrequests = infile.read().split(';')
            for sqlrequests in sqlrequests:
                if sqlrequests.strip():
                    self.cursor.execute(sqlrequests)

        print("ok")

        self.creat_table()

    def creat_table(self):

        self.cursor = self.connexion.cursor()

        database = join(dirname(dirname(abspath(__file__))), "settings", "sauvegarde.sql")
        print(database)
        with open(database) as infile:
            sqlrequests = infile.read().split(';')
            for sqlrequests in sqlrequests:
                if sqlrequests.strip():
                    self.cursor.execute(sqlrequests)



        


            