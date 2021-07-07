from models.entities.category import Category
from models.entities.brand import Brand 
from models.entities.store import Store


class Product:

    """class permettant d'initalisé les objets products"""

    def __init__(self, name, nutriscore, categories_list, url, brands_list, stores_list, id=None):
        self.id = id
        self.name = name
        self.nutriscore = nutriscore
        self.categories = categories_list
        self.url = url
        self.brands = brands_list
        self.stores = stores_list
        if id is None:
            self.split_cat()
            self.split_brands()
            self.split_stores()

    def split_cat(self):
        list_cat_split = self.categories.split(',')
        self.categories = [Category(x) for x in list_cat_split]

    def split_brands(self):
        list_brands_split = self.brands.split(',')
        self.brands = [Brand(x) for x in list_brands_split]

    def split_stores(self):
        list_stores_split = self.stores.split(',')
        self.stores = [Store(x) for x in list_stores_split]

        

  
