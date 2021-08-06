"""this module allows you to interact with the products's table"""

import mysql.connector

from models.entities.category import Category
from models.entities.product import Product
from models.entities.brand import Brand
from models.entities.store import Store
from models.entities.storeproduct import StoreProduct
from models.entities.brandproduct import BrandProduct
from models.entities.categoryproduct import CategoryProduct

from models.managers.manager import Manager
from models.managers.storesproductsmanager import StoresProductsManager
from models.managers.brandsmanager import BrandsManager
from models.managers.brandsproductsmanager import BrandsProductsManager
from models.managers.storesmanager import StoresManager
from models.managers.categoriesmanager import CategoriesManager
from models.managers.categoriesproductsmanager import CategoriesProductsManager

class ProductsManager(Manager):

    """class to communicate with table products and call the other manager. 
        Args:
        -Manager (class parent): initializes the connection to the database """

    def products_to_save(self, products):
        
        """méthode transformant les objects products en tuples 

        Args:
        - products (liste) : liste d'object product from apimanager

        Return : 
        - tup_products (liste) : tuple list with multiple items """
        
        tup_products = []
   
        for element in products: 
            tup_products.append((None, element.name, element.nutriscore, element.url))

        return tup_products

    def save_categories(self, products):

        """method transforming categories into tuple and calling the categoriesmanager to save it
        Args:
        - products (liste) : liste d'object product from apimanager

        Returns:
        - categories_save (liste) : object categories containing  id database
        """

        categoriesmanager = CategoriesManager()
        
        tup_categories = []
    
        for element in products:
            for catego in element.categories:
                tup_categories.append((None, catego.name))
        
        categories_save = categoriesmanager.save(tup_categories)

        return categories_save

    def save_brands(self, products):

        """method transforming brands into tuple and calling the brandsmanager to save it
        Args:
        - products (liste) : liste d'object product from apimanager

        Returns:
        - brands_save (liste) : object brands containing id database
        """

        brandsmanager = BrandsManager()

        tup_brands = []
    
        for element in products:
            for brand in element.brands:
                tup_brands.append((None, brand.name))
        
        brands_save = brandsmanager.save(tup_brands)

        return brands_save

    def save_stores(self, products):

        """method transforming brands into tuple and calling the storesmanager to save it
        Args:
        - products (liste) : liste d'object product from apimanager

        Returns:
        - stores_save (liste) : object stores containing id database
        """

        storesmanager = StoresManager()

        tup_stores = []
    
        for element in products:
            for store in element.stores:
                tup_stores.append((None, store.name))
        
        stores_save = storesmanager.save(tup_stores)

        return stores_save

    def save_products(self, products):

        """method to save and retrieve data in the products table
        Args : 
        - products (liste) : liste d'object product from apimanager
        
        returns:
        - brands_save (liste) : products with id from database """

        products_tup = self.products_to_save(products)
        
        sql = "INSERT INTO products (id, name, nutriscore, url) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE name = name"

        self.cursor.executemany(sql, products_tup)

        self.connexion.commit()

        self.cursor.close()

        self.cursor = self.connexion.cursor()

        name_product = []
        for element in products_tup:
            name_product.append(element[1])

        names = tuple(name_product)

        query= (
            "SELECT * FROM products "
            f"WHERE name IN ({', '.join('%s' for _ in names)})" 
        )
        self.cursor.execute(query, names)
    
        products_database = self.cursor.fetchall()

        products_save = []

        for element in products_database:
            products_save.append(Product(element[1], element[2], None, element[3], None, None, element[0]))
            
        return products_save
        

    def save_relationships(self, products):

        """make the connection between the various id and to call the corresponding manager to register them.

        Args:
        - products (liste) : liste d'object product from apimanager
        """

        categories_saved = self.save_categories(products)#changement type : categories / products / brands
        brands_saved = self.save_brands(products)
        stores_saved = self.save_stores(products)
        products_saved = self.save_products(products)
        
        productscategories = []
        productsbrands = []
        productstores = []

        for product in products_saved :#pour chauqe product dans la liste de produit avec des id numéroté 
            non_saved_product = next(filter(lambda prod: prod.name == product.name, products), None)#renvoie l'objet dans la liste d'objet python sans id numéroter avec le même nom avec true ou false
            if non_saved_product: #si c est True (renvoie quelques choses)
                for category in non_saved_product.categories:#pour la catégorie dans la liste de catégories de l'objet renvoyer
                    saved_category = next(filter(lambda cat: cat.name == category.name, categories_saved), None)#renvoie l'objet correspondant à la liste des objet categorie avec id numéroté
                    if saved_category: #si renvoie quelques choses
                        productscategories.append(CategoryProduct(product.id, saved_category.id)) #ajoute dans la liste (création d'objet categoryproduct)
                for brand in non_saved_product.brands:
                    saved_brands = next(filter(lambda bra: bra.name == brand.name, brands_saved), None)
                    if saved_brands:
                        productsbrands.append(BrandProduct(product.id, saved_brands.id))
                for store in non_saved_product.stores:
                    saved_stores = next(filter(lambda sto: sto.name == store.name, stores_saved), None)
                    if saved_stores:
                        productstores.append(StoreProduct(product.id, saved_stores.id))

        tup_productscategories = []
        tup_productsbrands = []
        tup_productstores = []

        for element in productscategories:
             tup_productscategories.append((element.id_product, element.id_category))
        categoriesproductsmanager = CategoriesProductsManager()
        categoriesproductsmanager.save(tup_productscategories)
        
        for element in productsbrands:
            tup_productsbrands.append((element.id_products, element.id_brands))
        brandsproductsmanager = BrandsProductsManager()
        brandsproductsmanager.save(tup_productsbrands)

        for element in productstores:
            tup_productstores.append((element.id_products, element.id_stores))
        storesproductsmanager = StoresProductsManager()
        storesproductsmanager.save(tup_productstores)


