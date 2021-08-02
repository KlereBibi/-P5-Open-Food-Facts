"""this module allows you to interact with the categories's table"""

import mysql.connector
from models.managers.manager import Manager
from models.entities.category import Category


class CategoriesManager(Manager):

    """class to communicate with table brands
        Args:
        -Manager (class parent): initializes the connection to the database """

    def save(self, categories):

        """method to save and retrieve data in the categories table
        Args : 
        - categories (liste) : tuple of categories to save
        
        returns:
        - categories_saved (liste) : categories with id from database """

        sql = "INSERT INTO categories (id, name) VALUES (%s, %s) ON DUPLICATE KEY UPDATE name=name"

        self.cursor.executemany(sql, categories)

        self.connexion.commit()

        self.cursor.close()

        self.cursor = self.connexion.cursor()

        name_categories = []
        for element in categories:
            name_categories.append(element[1])

        names = tuple(name_categories)
        query= (
            "SELECT * FROM categories "
            f"WHERE name IN ({', '.join('%s' for _ in names)})" 
        )
        self.cursor.execute(query, names)
    
        categories_database = self.cursor.fetchall()

        categories_saved = []
        for element in categories_database:
            categories_saved.append(Category(element[1], element[0]))

        return categories_saved

        self.cursor.close()

    def search_categories(self):

        sql = "SELECT * FROM categories "
        
        self.cursor.execute(sql)

        categories = self.cursor.fetchall()

        return categories

        self.cursor.close()



    

    
   