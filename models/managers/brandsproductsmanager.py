"""this module allows you to interact with the brandsproducts's table"""

from models.managers.manager import Manager
from models.entities.brand import Brand


class BrandsProductsManager(Manager):

    """class to communicate with table brandsproducts
        Args:
        -Manager (class parent): initializes the connection to the database """

    def save(self, brandsproducts):

        """method to save data in the brandsproducts table
        Args : 
        - brandsproducts (liste) : tuple with id_brands and id_products """

        sql = "INSERT INTO brands_products (id_products, id_brands)\
             VALUES (%s, %s)"

        self.cursor.executemany(sql, brandsproducts)

        self.connexion.commit()

    def find(self, substitute):

        self.cursor.execute("SELECT b.name FROM brands as b INNER JOIN brands_products AS bp ON b.id = bp.id_brands WHERE bp.id_products =%(id_product)s", {'id_product' : substitute.id})

        brands = self.cursor.fetchall()

        l_brand = []

        for element in brands:
            brand = Brand( element[0], None)
            l_brand.append(brand)

        return l_brand
