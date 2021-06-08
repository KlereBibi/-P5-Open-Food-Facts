from category import Category


class Product:

    """class permettant d'initalisé les objets products"""

    def __init__(self, name, nutriscore, categories_list, url, id=None, ):
        self.id = id
        self.name = name
        self.nutriscore = nutriscore
        self.categories = categories_list
        self.url = url
        if id is None:
            self.split_cat()

    def split_cat(self):
        list_cat_split = self.categories.split(',')
        self.categories = [Category(x) for x in list_cat_split]

        

  
