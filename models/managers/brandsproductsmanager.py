"""this module allows you to interact with the brandsproducts's table"""

from models.managers.manager import Manager


class BrandsProductsManager(Manager):

    """class to communicate with table brandsproducts
        Args:
        -Manager (class parent): initializes the connection to the database """

    def save(self, brandsproducts):

        """method to save data in the brandsproducts table
        Args:
        - brandsproducts (liste) : tuple with id_brands and id_products """

        cursor = self.connexion.cursor()
        sql = "INSERT INTO brands_products (id_products, id_brands)\
             VALUES (%s, %s)"

        cursor.executemany(sql, brandsproducts)

        super().end_request(cursor)
