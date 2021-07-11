"""this module allows you to interact with the storesproducts's table"""

from models.managers.manager import Manager

class StoresProductsManager(Manager):

    def save_storesproducts(self, storesproducts):
        
        """method to save data in the storesproducts table
        Args : 
        - storesproducts (liste) : tuple with id_products and id_stores
        """

        sql = "INSERT INTO stores_products (id_products, id_stores) VALUES (%s, %s)"
    
        self.cursor.executemany(sql, stores)

        self.connexion.commit()

        print(self.cursor.rowcount, "ligne insérée.")
