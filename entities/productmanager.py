from category import Category
from categorymanager import CategoryManager
from constante import REGISTERCATEGORIES
from constante import REGISTERPRODUCT
from connexion import ConnexionOff
import mysql.connector

class ProductManager:

    def save_product_tup(self, list):
        
        #creation de liste de tuple
        list_tup_prod = []
        categomanager = CategoryManager()
        #transformation en tuples
        for element in list: 
            list_tup_prod.append((None, element.name, element.nutriscore, element.url))
            for catego in element.categories:
                categomanager.list_tup_catego.append((None, catego.name))
        
        categomanager.save_catego_table()

        return list_tup_prod

    def save_in_table(self, list):

        connex = ConnexionOff()

        connex.save_table(REGISTERPRODUCT, self.save_product_tup(list))
        
 