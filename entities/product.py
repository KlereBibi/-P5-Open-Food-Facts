class Product:

    """class permettant d'initalisé les objets products"""

    def __init__(self, name, nutriscore, cat):
        self.id = None
        self.name = name
        self.nutriscore = nutriscore
        self.categories = cat
        self.list_cat_split= [] #je n'ai pas réussis à modifier directement categories
        self.url = None

    def split_cat(self):

        """méthode permettant de spliter le retour de chaine de caractère des categories"""
        
        self.list_cat_split = self.categories.split(',') #todo
        
     

  
