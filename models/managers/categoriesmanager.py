"""this module allows you to interact with the categories's table"""

from models.managers.manager import Manager
from models.entities.category import Category


class CategoriesManager(Manager):

    """class to communicate with table brands
        Args:
        -Manager (class parent): initializes the connection to the database """

    def save(self, categories):

        """method to save and retrieve data in the categories table
        Args:
        - categories (liste) : tuple of categories to save
        returns:
        - categories_saved (liste) : categories with id from database."""

        cursor = self.connexion.cursor()
        sql = "INSERT INTO categories (id, name) \
               VALUES (%s, %s) ON DUPLICATE KEY UPDATE name=name"

        cursor.executemany(sql, categories)
        super().end_request(cursor)

        cursor = self.connexion.cursor()

        name_categories = []
        for element in categories:
            name_categories.append(element[1])

        names = tuple(name_categories)
        query = (
            "SELECT * FROM categories "
            f"WHERE name IN ({', '.join('%s' for _ in names)})"
        )
        cursor.execute(query, names)
        categories_database = cursor.fetchall()
        super().end_request(cursor)

        categories_saved = []
        for element in categories_database:
            categories_saved.append(Category(element[1], element[0]))

        return categories_saved

    def search_categories(self):

        """method allowing to retrieve the categories present in the database
        return : list of object categories"""

        cursor = self.connexion.cursor()
        sql = "SELECT * FROM categories "

        cursor.execute(sql)
        categories = cursor.fetchall()
        super().end_request(cursor)

        categories_saved = []

        for element in categories:
            categories_saved.append(Category(element[1], element[0]))

        return categories_saved
