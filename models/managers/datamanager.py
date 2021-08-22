
"""module to delete and creat tables in database """

from models.managers.manager import Manager
import string


class DataManager(Manager):

    """class to communicate with table brandsproducts
        Args:
        -Manager (class parent): initializes the connection to the database """

    def delete_tables(self):

        """method to drop all tables in the database
        by reading a file containing sql commands."""

        super().read_command_sql("deletetables.sql")

        self.creat_table()

    def creat_table(self):

        """method to creat all tables in the database
        by reading a file containing sql commands."""

        super().read_command_sql("sauvegarde.sql")

    def search_tables(self):

        """method allowing to know if the database contains tables 
        and if these tables contain elements
        return database_empty(bol): 
            True (condition if not table or element) 
            or False(if database have table and element in table) """

        cursor = self.connexion.cursor()
        sql = "SHOW TABLES;"
        cursor.execute(sql)
        tables = cursor.fetchall()
        super().end_request(cursor)

        database_empty = False
        if len(tables) == 8:
            for element in tables:
                element = ''.join([i for i in element if i not in string.punctuation])
                if element != "substitute":
                    cursor = self.connexion.cursor()
                    cursor.execute("SELECT count(*) FROM {}".format(element))#à rectifier
                    result = cursor.fetchall()
                    self.end_request(cursor)
                    result = ''.join([i for i in str(result[0]) if i not in string.punctuation])
                    if int(result[0]) != 0:
                        continue
                    else:
                        database_empty = True
        else:
            database_empty = True

        return database_empty
        