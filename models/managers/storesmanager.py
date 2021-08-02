"""this module allows you to interact with the stores's table"""

import mysql.connector
from models.managers.manager import Manager
from models.entities.store import Store

class StoresManager(Manager):

    """class to communicate with table stores
        Args:
        -Manager (class parent): initializes the connection to the database """
    
    def save(self, stores):

        """method to save and retrieve data in the stores table
        Args : 
        - stores (liste) : tuple of stores to save
        
        returns:
        - stores_save (liste) : stores with id from database """

        sql = "INSERT INTO stores (id, name) VALUES (%s, %s) ON DUPLICATE KEY UPDATE name=name"

        self.cursor.executemany(sql, stores)

        self.connexion.commit()

        self.cursor.close()

        self.cursor = self.connexion.cursor()

        name_stores = []
        for element in stores:
            name_stores.append(element[1])

        names = tuple(name_stores)
        query= (
            "SELECT * FROM stores "
            f"WHERE name IN ({', '.join('%s' for _ in names)})" #comprends pas tout
        )
        self.cursor.execute(query, names)
    
        stores_database = self.cursor.fetchall()

        stores_save = []
        for element in stores_database :
            stores_save.append(Store(element[1], element[0]))

        return stores_save
