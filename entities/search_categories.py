import requests, json

class search_product:

    def __init__(self):

        self.category_dict_list = []
        self.six_first_category = []

    def search_in_openfood(self):

        r = requests.get("https://fr.openfoodfacts.org/categories.json")
        result = json.loads(r.text)
        self.category_dict_list.append(result['tags'])

    def take_six_first_categories(self):
        n = 0
        for element in self.category_dict_list:
            for each in element: 
                self.six_first_category.append(each)
                n+=1
                if n == 6:
                    break
    
    def print_categories(self):
        for element in self.six_first_category:
            print(element['name'])
        
off = search_product()
off.search_in_openfood()
off.take_six_first_categories()
off.print_categories()



    