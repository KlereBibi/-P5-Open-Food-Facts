"""module initializing product """

from models.entities.category import Category
from models.entities.brand import Brand 
from models.entities.store import Store


class Product:

    """class to create a products object"""

    def __init__(self, name, nutriscore=None, categories=None, url=None, brands=None, stores=None, id=None):

        """class to create a product object
            Args:
        - name (str) : name of product
        - nutriscore (str) : note of nutriscore 
        - categories (str) : all product categories in chain of character
        - url (str) : link to find the product on openfoodfac
        - brands (str) : all product brands in chain of character
        - stores (stre) : all product stores in chain of character
        - id (int) : value None or from Database
        
        use of a condition to call methods allowing the creation of list of stores, brands and categories object
        """

        self.id = id
        self.name = name
        self.nutriscore = nutriscore
        self.categories = categories
        self.url = url
        self.brands = brands
        self.stores = stores
        if id is None:
            self.split_cat()
            self.split_brands()
            self.split_stores()

    def split_cat(self):

        
        """"split string of characters in liste and call class category to creat object category """
        list_cat_split = self.categories.split(',')
        self.categories = [Category(x) for x in list_cat_split]

    def split_brands(self):

        """"split string of characters in liste and call class category to creat object brand"""

        list_brands_split = self.brands.split(',')
        self.brands = [Brand(x) for x in list_brands_split]

    def split_stores(self):

        """"split string of characters in liste and call class category to creat object store """

        list_stores_split = self.stores.split(',')
        self.stores = [Store(x) for x in list_stores_split]

        

  
