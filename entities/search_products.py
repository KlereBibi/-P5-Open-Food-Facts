import requests
from constant import category


class search_product:

    def __init__(self):

        self.category_dict_list = []

    def pouet(self):
        for element in category:
            r = requests.get("https://fr.openfoodfacts.org/categorie/{}.json".format(element), auth=('user', 'pass'))
            self.category_dict_list.append({ element : r.text })
    
    def print(self):
        for element in self.category_dict_list:
            print(element)

chouette = search_product()
chouette.pouet()
chouette.print()

