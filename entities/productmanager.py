from category import Category
from categorymanager import CategoryManager
from manager import Manager
from product import Product
from categoryproduct import CategoryProduct
from categoryproductmanager import CategoryProductManager
import mysql.connector

class ProductManager(Manager):


    def save_product_tup(self, liste):
        
        """ méthode pour transformer les objets products en tuples. 
        initialisation de l'objet category manager pour ajouter dans la liste du constructeur les tuples des categories
        appel de la fonction pour enregistrer les catégories 
        return la liste de tuples """

        #creation de liste de tuple
        
        list_tup_prod = []
        
        
        #transformation en tuples
        for element in liste: 
            list_tup_prod.append((None, element.name, element.nutriscore, element.url))

        return list_tup_prod

    def save_catego(self, liste):

        categomanager = CategoryManager()
        list_tup_catego = []
    
        for element in liste:
            for catego in element.categories:
                list_tup_catego.append((None, catego.name))
        
        list_tup_id_catego = categomanager.save_catego_table(list_tup_catego)

        return list_tup_id_catego

    def save_in_table(self, liste):

        """méthode enregistrant la liste des produits dans la base off en appelant la class mère"""

        products_list = self.save_product_tup(liste)#retourne la liste des tup produits
        
        
        sql = "INSERT INTO products (id, name, nutriscore, url) VALUES (%s, %s, %s, %s)"

        value = products_list

        self.cur.executemany(sql, value)

        self.connexion_off.commit()

        print(self.cur.rowcount, "ligne insérée.")

        self.cur.close()

        self.cur = self.connexion_off.cursor()

        liste_name_product = []
        for element in products_list:
            liste_name_product.append(element[1])#je prends que les noms enregistrer

        names = tuple(liste_name_product)#j'en fais un grand tuple

        query= (
            "SELECT * FROM products "
            f"WHERE name IN ({', '.join('%s' for _ in names)})" #comprends pas tout
        )
        self.cur.execute(query, names)
    
        res = self.cur.fetchall()#je récupère la donnée sous forme de tuple

        liste_o_product_id = []

        for element in res:
            liste_o_product_id.append(Product(element[1], element[2], None, element[3], element[0]))
            
        return liste_o_product_id
        #la problématique : je peux avoir deux fois un même produit dans deux catégories différentes - 

    def bonde_id_catego_product(self, liste):

        liste_o_catego_id = self.save_catego(liste)
        liste_o_product_id = self.save_in_table(liste)

        liste_o_bonde = []

        for element in liste_o_product_id:
            lobj = [x for x in liste if x.name == element.name]#liste des objets products correspondant au nom de l'élément
            for each in lobj:
                lobj2 = [x for x in each.categories]#liste des objets categories de chaque product
                for i in lobj2:
                    lobj3 = [x for x in liste_o_catego_id if x.name == i.name]#liste retournant les catégories 
                    for e in lobj3:
                        liste_o_bonde.append(CategoryProduct(element.id, e.id))#pour chaque obket dans la liste retournant le catégorie avec non none correspondant au product, ajoute dans la liste id_product avec _id categorie

        liste_tup_bonde = []

        for element in liste_o_bonde:
            liste_tup_bonde.append((element.id_product, element.id_categories))#transformation en tuple pour l'enregistrement dans une liste pour la requête

        categoproductmana = CategoryProductManager()

        categoproductmana.save_bond_cp_table(liste_tup_bonde)
                    
