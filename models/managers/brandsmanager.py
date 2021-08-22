"""this module allows you to interact with the brands's table"""

from models.managers.manager import Manager
from models.entities.brand import Brand


class BrandsManager(Manager):

    """class to communicate with table brands
        Args:
        -Manager (class parent): initializes the connection to the database """

    def save(self, brands):

        """method to save and retrieve data in the brands table
        Args:
        - brands (liste) : tuple of brands to save
        returns:
        - brands_save (liste) : brands with id from database."""
        self.connexion.reconnect()

        cursor = self.connexion.cursor()
        sql = "INSERT INTO brands (id, name) \
               VALUES (%s, %s) ON DUPLICATE KEY UPDATE name=name"

        cursor.executemany(sql, brands)

        self.connexion.commit()

        cursor.close()

        self.connexion.close()

        self.connexion.reconnect()

        cursor = self.connexion.cursor()

        name_brands = []
        for element in brands:
            name_brands.append(element[1])

        names = tuple(name_brands)
        query = (
            "SELECT * FROM brands "
            f"WHERE name IN ({', '.join('%s' for _ in names)})"
        )
        cursor.execute(query, names)

        brands_database = cursor.fetchall()
        self.connexion.commit()
        cursor.close()
        self.connexion.close()

        brands_save = []
        for element in brands_database:
            brands_save.append(Brand(element[1], element[0]))

        return brands_save
