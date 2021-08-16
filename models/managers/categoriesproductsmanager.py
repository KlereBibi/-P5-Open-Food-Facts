"""this module allows you to interact with the categoriesproducts table"""

from models.managers.manager import Manager


class CategoriesProductsManager(Manager):

    """class to communicate with table categoriesproducts
        Args:
        -Manager (class parent): initializes the connection to the database """

    def save(self, tup_categoriesproducts):

        """method to save data in the brandsproducts table
        Args:
        - categoriesproducts (liste) : tuple with id_products and id_categories
        """

        sql = "INSERT INTO categories_products (id_products, id_categories) \
               VALUES (%s, %s)"

        self.cursor.executemany(sql, tup_categoriesproducts)

        self.connexion.commit()
