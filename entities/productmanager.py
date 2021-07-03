from category import Category
from manager import Manager
from product import Product
from brand import Brand
from store import Store
from storeproduct import StoreProduct
from storeproductmanager import StoreProductManager
from brandmanager import BrandManager
from brandproduct import BrandProduct
from brandproductmanager import BrandProductManager
from storemanager import StoreManager
from categorymanager import CategoryManager
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

    def save_brands(self,liste):

        brandmanager = BrandManager()

        list_tup_brand = []
    
        for element in liste:
            for brand in element.brands:
                list_tup_brand.append((None, brand.name))
        
        list_tup_id_brands = brandmanager.save_brand_table(list_tup_brand)

        return list_tup_id_brands


    def save_stores(self, liste):

        storemanager = StoreManager()

        list_tup_store = []
    
        for element in liste:
            for store in element.stores:
                list_tup_store.append((None, store.name))
        
        list_tup_id_stores = storemanager.save_store_table(list_tup_store)

        return list_tup_id_stores

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
            liste_o_product_id.append(Product(element[1], element[2], None, element[3], None, None, element[0]))
            
        return liste_o_product_id
        #la problématique : je peux avoir deux fois un même produit dans deux catégories différentes - 

    def bonde_id_catego_product(self, liste):

        liste_o_catego_id = self.save_catego(liste)


        liste_o_product_id = self.save_in_table(liste)



        liste_o_brand_id = self.save_brands(liste)


        liste_o_store_id = self.save_stores(liste)

        liste_o_bonde_procat = []

        liste_o_bonde_probra = []

        liste_o_bonde_prosto = []

        for product in liste_o_product_id:#pour chauqe product dans la liste de produit avec des id numéroté 
            non_saved_product = next(filter(lambda prod: prod.name == product.name, liste), None)#renvoie l'objet dans la liste d'objet python sans id numéroter avec le même nom avec true ou false
            if non_saved_product: #si c est True (renvoie quelques choses)
                for category in non_saved_product.categories:#pour la catégorie dans la liste de catégories de l'objet renvoyer
                    saved_category = next(filter(lambda cat: cat.name == category.name, liste_o_catego_id), None)#renvoie l'objet correspondant à la liste des objet categorie avec id numéroté
                    if saved_category: #si renvoie quelques choses
                        liste_o_bonde_procat.append(CategoryProduct(product.id, saved_category.id)) #ajoute dans la liste (création d'objet categoryproduct)
                for brand in non_saved_product.brands:
                    saved_brands = next(filter(lambda bra: bra.name == brand.name, liste_o_brand_id), None)
                    if saved_brands:
                        liste_o_bonde_probra.append(BrandProduct(product.id, saved_brands.id))
                for store in non_saved_product.stores:
                    saved_stores = next(filter(lambda sto: sto.name == store.name, liste_o_store_id), None)
                    if saved_stores:
                        liste_o_bonde_prosto.append(StoreProduct(product.id, saved_stores.id))


        liste_tup_bonde_procat = []
        liste_tup_bonde_probra = []
        liste_tup_bonde_prosto = []

        for element in liste_o_bonde_procat:
            liste_tup_bonde_procat.append((element.id_product, element.id_categories))#transformation en tuple pour l'enregistrement dans une liste pour la requête

        categoproductmana = CategoryProductManager()

        categoproductmana.save_bond_cp_table(liste_tup_bonde_procat)
        
        for element in liste_o_bonde_probra:
            liste_tup_bonde_probra.append((element.id_products, element.id_brands))
        
        brandpromana = BrandProductManager()

        brandpromana.save_bond_bp_table(liste_tup_bonde_probra)

        for element in liste_o_bonde_prosto:
            liste_tup_bonde_prosto.append((element.id_products, element.id_stores))

        storepromana = StoreProductManager()

        storepromana.save_bond_sp_table(liste_tup_bonde_prosto)

        
