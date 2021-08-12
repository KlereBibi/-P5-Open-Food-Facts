"""this module allows you to interact with the storesproducts's table"""

from models.managers.manager import Manager
from models.entities.store import Store


class StoresProductsManager(Manager):

    """class to communicate with table StoresProductsManager
        Args:
        -Manager (class parent): initializes the connection to the database """

    def save(self, storesproducts):

        """method to save data in the storesproducts table
        Args:
        - storesproducts (liste) : tuple with id_products and id_stores"""

        sql = "INSERT INTO stores_products (id_products, id_stores)\
             VALUES (%s, %s)"

        self.cursor.executemany(sql, storesproducts)

        self.connexion.commit()

    def find(self, substitute):
    
        self.cursor.execute("SELECT s.name FROM stores as s INNER JOIN stores_products AS sp ON s.id = sp.id_stores WHERE sp.id_products =%(id_product)s", {'id_product' : substitute.id})

        stores = self.cursor.fetchall()

        l_stores = []

        for element in stores:
            store = Store( element[0], None)
            l_stores.append(store)

        return l_stores
