import requests, json
import re

class ApiManager:

    def search_category(self):

        r = requests.get("https://fr.openfoodfacts.org/categories.json")
        result = json.loads(r.text)
        list_dict_category = result['tags']
       
        list_dict_category.sort(key=lambda x: x["products"], reverse=True)
        
        return list_dict_category[:6]
    
    def print_categories(self):
        for element in self.search_category():
            print(element['name'])

    def search_products(self):

        r = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=Snacks&page_size=1&json=1")
        result = json.loads(r.text)
        list_dict_product = result['products']
        return list_dict_product[:10]






    