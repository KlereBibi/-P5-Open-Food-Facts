import requests
from constant import CATEGORY #majuscule


class search_product:

    def __init__(self):

        self.category_dict_list = []

    def search_in_openfood(self):
        for element in CATEGORY:
            r = requests.get("https://fr.openfoodfacts.org/categorie/{}.json".format(element))#non -> pas bon endpoint -> permets de préciser combien de produits
            self.category_dict_list.append({ element : r })#url qui va pas juste 
    
    def print_search_result(self):
        for element in self.category_dict_list:
            print(element)

chouette = search_product()
chouette.search_in_openfood()
chouette.print_search_result()

