
import requests, json 
from models.entities.product import Product
from models.entities.categoryproduct import CategoryProduct
from models.managers.manager import Manager
from models.managers.productmanager import ProductManager


"""requests : permet d'envoyer une requête GET à l'API"""
"""json : sera utiliser avec json.loads pour deserialiser le texte contenant du json vers un objet Python en utilisant une table de conversion"""

class ApiManager(Manager):


    """Création d'une class gérant la connexion à l'API d'open food fact"""

    def search_categories_with_api(self):

        """méthode utilisant request pour aller chercher les informations
        transformation du fichier json en objet python
        enregistrement du résultat voulu dans une liste
        return une liste avec les 6 premières catégories"""

        search_categories = requests.get("https://fr.openfoodfacts.org/categories.json")
        read = json.loads(search_categories.text)
        list_dict_categories = read['tags']
        list_dict_categories.sort(key=lambda x: x["products"], reverse=True)
        return list_dict_categories[:6]

    def save_name_categories(self):
        
        """ méthode permettant de retourner la liste de nom des 6 catégories ayant le + de produits"""
        name_cate = []
        for element in self.search_categories_with_api():
            name_cate.append(element['name'])
        
        return name_cate

    def search_product_in_categories(self):
    
        """méthode pour chercher les 10 premiers produits des 6 premières catégories
        retourne une list contenant des listes de dictionnaires de produuits"""
        list_all_product = []
        for element in self.save_name_categories():
            r = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={}&page_size=1&json=1".format(element))
            result = json.loads(r.text)
            list_all_product.append(result['products'][:1])

        return list_all_product

    def creat_product(self):

        """methode générant des objets product et les enregistrant dans une liste retourner"""
    
        list_o_product_no_id = []
        for element in self.search_product_in_categories():
            for item in element:
                newprod = Product(item['product_name_fr'], item['nutriscore_grade'], item['categories'], item['url'], item['brands'], item['stores'])
                list_o_product_no_id.append(newprod)    
        
        return list_o_product_no_id

    def save_in_database(self):

        promana = ProductManager()
        promana.save_bonde_database(self.creat_product())
       



    
   
