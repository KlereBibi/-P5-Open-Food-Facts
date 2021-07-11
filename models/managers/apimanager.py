"""this module queries the OpenFoodFac API and retrieves the targeted data. """

import requests, json 
from models.entities.product import Product
from models.entities.categoryproduct import CategoryProduct
from models.managers.manager import Manager
from models.managers.productsmanager import ProductsManager

class ApiManager(Manager):

    """Class used to query the API, retrieve data, process it and send it to the product manager."""

    def search_categories(self):

        """Method querying the OpenFoodFac API to retrieve categories.
        Methode sort them by increasing popularity. 
        returns : 
        - name_categories (liste) : list name of the first six categories"""

        categories_find = requests.get("https://fr.openfoodfacts.org/categories.json")
        read = json.loads(categories_find.text)
        categories = read['tags']
        categories.sort(key=lambda x: x["products"], reverse=True)
        six_categories = categories[:6]
        name_categories = []
        for element in six_categories:
            name_categories.append(element['name'])
        
        return name_categories

    def search_products(self):
    
        """ Method requesting the OpenFoodFac API to find the products with the category list.
        The method registers products with the Product class.
        returns : 
        - products (liste) : list of product with ID = None."""

        products_saved = []
        products = []
        for element in self.search_categories():
            products_find= requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={}&page_size=1&json=1".format(element))
            result = json.loads(products_find.text)
            products_saved.append(result['products'][:1])

        for element in products_saved:
            for item in element:
                newprod = Product(item['product_name_fr'], item['nutriscore_grade'], item['categories'], item['url'], item['brands'], item['stores'])
                products.append(newprod)    

        return products

    def save_data(self):

        """method calling the product manager module to sort and save the data in the database"""

        productmanager = ProductsManager()
        productmanager.save_relationships(self.search_products())
       