"""this module allows you to interact with the categoriesproducts table"""

import mysql.connector
from models.managers.manager import Manager

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

    def search_product(self, userchoice):
        
        # self.cursor.execute("SELECT id_products FROM categories_products WHERE id_categories=%(id_categories)s",
        # {'id_categories': userchoice})

        # products = self.cursor.fetchall()

        # self.cursor.close()

        # products_liste = []

        self.cursor = self.connexion.cursor()

      
        self.cursor.execute("SELECT DISTINCT products.id, products.name FROM products INNER JOIN categories_products ON products.id = categories_products.id_products WHERE categories_products.id_products IN (SELECT DISTINCT id_products FROM categories_products WHERE id_categories=%(id_categories)s) ",
        {'id_categories': userchoice})

        name_products = self.cursor.fetchall()

        return name_products