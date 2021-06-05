import requests, json 
from product import Product
from productmanager import ProductManager
"""requests : permet d'envoyer une requête GET à l'API"""
"""json : sera utiliser avec json.loads pour deserialiser le texte contenant du json vers un objet Python en utilisant une table de conversion"""

class ApiManager:


    """Création d'une class gérant la connexion à l'API d'open food fact"""

    def search_cat_important(self):

        """méthode utilisant request pour aller chercher les informations
        transformation du fichier json en objet python
        enregistrement du résultat voulu dans une liste
        return une liste avec les 6 premières catégories"""

        r = requests.get("https://fr.openfoodfacts.org/categories.json")
        result = json.loads(r.text)
        list_dict_cate = result['tags']
        list_dict_cate.sort(key=lambda x: x["products"], reverse=True)
        return list_dict_cate[:6]

    def print_cat_important(self):
        
        """ méthode permettant de retourner la liste de nom des 6 catégories ayant le + de produits"""
        name_cate = []
        for element in self.search_cat_important():
            name_cate.append(element['name'])
        
        return name_cate

    def search_prod(self):
    
        """méthode pour chercher les 10 premiers produits des 6 premières catégories
        retourne une list contenant des listes de dictionnaires de produuits"""
        list_all_prod = []
        for element in self.print_cat_important():
            r = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={}&page_size=1&json=1".format(element))
            result = json.loads(r.text)
            list_all_prod.append(result['products'][:1])

        return(list_all_prod)

    def creat_prod(self):

        """methode générant des objets product et les enregistrant dans une liste retourner"""
    
        my_list_prod = []
        for element in self.search_prod():
            for item in element:
                newprod = Product(item['product_name_fr'], item['nutriscore_grade'], item['categories'], item['url'])
                my_list_prod.append(newprod)    
        
        return my_list_prod

    def call_promana(self):

        promana = ProductManager()
        promana.save_product(self.creat_prod())

a = ApiManager()
a.call_promana()

    
   
