
"""module to delete and creat tables in database """

from models.managers.manager import Manager
from os.path import join, dirname, abspath

class DataManager(Manager):

    """class to communicate with table brandsproducts
        Args:
        -Manager (class parent): initializes the connection to the database """

    def delete_tables(self):

        """method to drop all tables in the database by reading a file containing sql commands"""
        
        super().read_command_sql("deletetables.sql")

        self.creat_table()

    def creat_table(self):

        """method to creat all tables in the database by reading a file containing sql commands"""

        super().read_command_sql("sauvegarde.sql")



        


            