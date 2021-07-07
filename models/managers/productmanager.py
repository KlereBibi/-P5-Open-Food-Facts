import mysql.connector

from models.entities.category import Category
from models.entities.product import Product
from models.entities.brand import Brand
from models.entities.store import Store
from models.entities.storeproduct import StoreProduct
from models.entities.brandproduct import BrandProduct
from models.entities.categoryproduct import CategoryProduct

from models.managers.manager import Manager
from models.managers.storeproductmanager import StoreProductManager
from models.managers.brandmanager import BrandManager
from models.managers.brandproductmanager import BrandProductManager
from models.managers.storemanager import StoreManager
from models.managers.categorymanager import CategoryManager
from models.managers.categoryproductmanager import CategoryProductManager

class ProductManager(Manager):


    def make_product_tup_list(self, liste_o_product_api):
        
        """ méthode pour transformer les objets products en tuples. 
        initialisation de l'objet category manager pour ajouter dans la liste du constructeur les tuples des categories
        appel de la fonction pour enregistrer les catégories 
        return la liste de tuples """
        
        list_tup_prod = []
   
        for element in liste_o_product_api: 
            list_tup_prod.append((None, element.name, element.nutriscore, element.url))

        return list_tup_prod

    def save_categories_with_manager(self, liste_o_product_api):

        categomanager = CategoryManager()
        
        list_tup_categories = []
    
        for element in liste_o_product_api:
            for catego in element.categories:
                list_tup_categories.append((None, catego.name))
        
        list_tup_id_catego = categomanager.save_categories_database(list_tup_categories)

        return list_tup_id_catego

    def save_brands_with_manager(self, liste_o_product_api):

        brandmanager = BrandManager()

        list_tup_brand = []
    
        for element in liste_o_product_api:
            for brand in element.brands:
                list_tup_brand.append((None, brand.name))
        
        list_tup_id_brands = brandmanager.save_brand_database(list_tup_brand)

        return list_tup_id_brands


    def save_stores_with_manager(self, liste_o_product_api):

        storemanager = StoreManager()

        list_tup_store = []
    
        for element in liste_o_product_api:
            for store in element.stores:
                list_tup_store.append((None, store.name))
        
        list_tup_id_stores = storemanager.save_store_database(list_tup_store)

        return list_tup_id_stores

    def save_product_database(self, liste_o_product_api):

        """méthode enregistrant la liste des produits dans la base off en appelant la class mère"""

        products_list = self.make_product_tup_list(liste_o_product_api)#retourne la liste des tup produits
        
        
        sql = "INSERT INTO products (id, name, nutriscore, url) VALUES (%s, %s, %s, %s)"

        value = products_list

        self.cursor.executemany(sql, value)

        self.connexion_database_off.commit()

        print(self.cursor.rowcount, "ligne insérée.")

        self.cursor.close()

        self.cursor = self.connexion_database_off.cursor()

        liste_name_product = []
        for element in products_list:
            liste_name_product.append(element[1])#je prends que les noms enregistrer

        names = tuple(liste_name_product)#j'en fais un grand tuple

        query= (
            "SELECT * FROM products "
            f"WHERE name IN ({', '.join('%s' for _ in names)})" #comprends pas tout
        )
        self.cursor.execute(query, names)
    
        product_id_name = self.cursor.fetchall()#je récupère la donnée sous forme de tuple

        liste_o_product_id = []

        for element in product_id_name:
            liste_o_product_id.append(Product(element[1], element[2], None, element[3], None, None, element[0]))
            
        return liste_o_product_id
        #la problématique : je peux avoir deux fois un même produit dans deux catégories différentes - 

    def save_bonde_database(self, liste_o_product_api):

        liste_o_catego_id = self.save_categories_with_manager(liste_o_product_api)
        liste_o_brand_id = self.save_brands_with_manager(liste_o_product_api)
        liste_o_store_id = self.save_stores_with_manager(liste_o_product_api)
        liste_o_product_id = self.save_product_database(liste_o_product_api)
        
        liste_id_productcategories = []
        liste_id_productbrand = []
        liste_id_productstore = []

        for product in liste_o_product_id:#pour chauqe product dans la liste de produit avec des id numéroté 
            non_saved_product = next(filter(lambda prod: prod.name == product.name, liste_o_product_api), None)#renvoie l'objet dans la liste d'objet python sans id numéroter avec le même nom avec true ou false
            if non_saved_product: #si c est True (renvoie quelques choses)
                for category in non_saved_product.categories:#pour la catégorie dans la liste de catégories de l'objet renvoyer
                    saved_category = next(filter(lambda cat: cat.name == category.name, liste_o_catego_id), None)#renvoie l'objet correspondant à la liste des objet categorie avec id numéroté
                    if saved_category: #si renvoie quelques choses
                        liste_id_productcategories.append(CategoryProduct(product.id, saved_category.id)) #ajoute dans la liste (création d'objet categoryproduct)
                for brand in non_saved_product.brands:
                    saved_brands = next(filter(lambda bra: bra.name == brand.name, liste_o_brand_id), None)
                    if saved_brands:
                        liste_id_productbrand.append(BrandProduct(product.id, saved_brands.id))
                for store in non_saved_product.stores:
                    saved_stores = next(filter(lambda sto: sto.name == store.name, liste_o_store_id), None)
                    if saved_stores:
                        liste_id_productstore.append(StoreProduct(product.id, saved_stores.id))


        liste_tup_id_productcategories = []
        liste_tup_id_productbrand = []
        liste_tup_id_productstore = []

        for element in liste_id_productcategories:
             liste_tup_id_productcategories.append((element.id_products, element.id_categories))
        categoproductmanage = CategoryProductManager()
        categoproductmanage.save_categoryproduct_database(liste_tup_id_productcategories)
        
        for element in liste_id_productbrand:
            liste_tup_id_productbrand.append((element.id_products, element.id_brands))
        brandpromanage = BrandProductManager()
        brandpromanage.save_brandpoduct_database(liste_tup_id_productbrand)

        for element in liste_id_productstore:
            liste_tup_id_productstore.append((element.id_products, element.id_stores))

        storepromanage = StoreProductManager()
        storepromanage.save_storeproduct_database(liste_tup_id_productstore)

        
