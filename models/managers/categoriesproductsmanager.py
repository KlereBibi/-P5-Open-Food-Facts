"""this module allows you to interact with the categoriesproducts table"""

import mysql.connector
from models.managers.manager import Manager
from models.entities.product import Product

class CategoriesProductsManager(Manager):

    """class to communicate with table categoriesproducts
        Args:
        -Manager (class parent): initializes the connection to the database """

    def save(self, tup_categoriesproducts):
        
        """method to save data in the brandsproducts table
        Args : 
        - categoriesproducts (liste) : tuple with id_products and id_categories
        """

        sql = "INSERT INTO categories_products (id_products, id_categories) VALUES (%s, %s)"

        self.cursor.executemany(sql, tup_categoriesproducts)

        self.connexion.commit()

    def search_products(self, userchoice):

        self.cursor = self.connexion.cursor()

        self.cursor.execute("SELECT p.id, p.name, p.nutriscore FROM products as p INNER JOIN categories_products as cp ON p.id = cp.id_products INNER JOIN categories as c on c.id = cp.id_categories WHERE c.id =%(id_categories)s", {'id_categories': userchoice})

        products = self.cursor.fetchall()

        products_saved = []

        for element in products:
            products_saved.append(Product(element[1], element[2], None, None, None, None, element[0]))
            

        return products_saved #bon endroit?

    