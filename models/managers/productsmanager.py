"""this module allows you to interact with the products's table"""

from models.entities.product import Product
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
from mysql import connector



class ProductsManager(Manager):

    """class to communicate with table products and call the other manager.
        Args:
        -Manager (class parent): initializes the connection to the database """

    def products_to_save(self, products):

        """méthode transformant les objects products en tuples.
        Args:
        -products (liste): liste d'object product from apimanager.
        Return:
        -tup_products (liste): tuple list with multiple items."""

        tup_products = []

        for element in products:
            tup_products.append((None, element.name,
                                 element.nutriscore,
                                 element.url))

        return tup_products

    def save_categories(self, products):

        """method transforming categories into tuple
        and calling the categoriesmanager to save it.
        Args:
        - products(liste): liste d'object product from apimanager

        Returns:
        - categories_save(liste): categories containing  id database"""

        categoriesmanager = CategoriesManager()

        tup_categories = []

        for element in products:
            for catego in element.categories:
                tup_categories.append((None, catego.name))

        categories_save = categoriesmanager.save(tup_categories)

        return categories_save

    def save_brands(self, products):

        """method transforming brands into tuple
        and calling the brandsmanager to save it
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

        """method transforming brands into tuple
        and calling the storesmanager to save it.
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
        Args:
        - products (liste) : liste d'object product from apimanager
        returns:
        - brands_save (liste) : products with id from database """

        products_tup = self.products_to_save(products)
        
        sql = "INSERT INTO products (id, name, nutriscore, url) \
                    VALUES (%s, %s, %s, %s) \
                    ON DUPLICATE KEY UPDATE name = name"

        self.cursor.executemany(sql, products_tup)

        self.connexion.commit()
        #except connector.errors.DatabaseError:

        self.cursor.close()

        self.cursor = self.connexion.cursor()

        names_products = []
        for element in products_tup:
            names_products.append(element[1])

        names = tuple(names_products)

        query= (
            "SELECT * FROM products "
            f"WHERE name IN ({', '.join('%s' for _ in names)})"
            )
        self.cursor.execute(query, names)
        products_database = self.cursor.fetchall()
 
        self.cursor.close()

        products_save = []

        for element in products_database:
            products_save.append(Product(element[1],
                                         element[2],
                                         None,
                                         element[3],
                                         None, None,
                                         element[0]))

        return products_save

    def save_relationships(self, products):

        """make the connection between the various id
        and to call the corresponding manager to register them.
        Args:
        - products (liste) : liste d'object product from apimanager"""

        categories_saved = self.save_categories(products)
        brands_saved = self.save_brands(products)
        stores_saved = self.save_stores(products)
        products_saved = self.save_products(products)

        productscategories = []
        productsbrands = []
        productstores = []

        for product in products_saved:
            non_saved_product = next(filter(lambda prod:
                                            prod.name == product.name,
                                            products), None)
            if non_saved_product:
                for category in non_saved_product.categories:
                    saved_category = next(filter(lambda cat:
                                                 cat.name == category.name,
                                                 categories_saved),
                                          None)
                    if saved_category:
                        productscategories. \
                            append(CategoryProduct(product.id,
                                                   saved_category.id))
                for brand in non_saved_product.brands:
                    saved_brands = next(filter(lambda bra:
                                               bra.name == brand.name,
                                               brands_saved), None)
                    if saved_brands:
                        productsbrands.append(BrandProduct(product.id,
                                                           saved_brands.id))
                for store in non_saved_product.stores:
                    saved_stores = next(filter(lambda sto:
                                               sto.name == store.name,
                                               stores_saved), None)
                    if saved_stores:
                        productstores.append(StoreProduct(product.id,
                                                          saved_stores.id))

        tup_productscategories = []
        tup_productsbrands = []
        tup_productstores = []

        for element in productscategories:
            tup_productscategories.append((element.id_product,
                                           element.id_category))
        categoriesproductsmanager = CategoriesProductsManager()
        categoriesproductsmanager.save(tup_productscategories)

        for element in productsbrands:
            tup_productsbrands.append((element.id_products,
                                       element.id_brands))
        brandsproductsmanager = BrandsProductsManager()
        brandsproductsmanager.save(tup_productsbrands)

        for element in productstores:
            tup_productstores.append((element.id_products,
                                      element.id_stores))
        storesproductsmanager = StoresProductsManager()
        storesproductsmanager.save(tup_productstores)

    def search_products(self, userchoice):

        """method requesting in the database
        to find the products present in the categories
        selected by the user.
        returns (liste): bjects products """

        self.cursor = self.connexion.cursor()

        self.cursor.execute("SELECT p.id, p.name, p.nutriscore \
                             FROM products as p \
                             INNER JOIN categories_products as cp \
                             ON p.id = cp.id_products \
                             INNER JOIN categories as c \
                             ON c.id = cp.id_categories \
                             WHERE c.id =%(id_categories)s",
                            {'id_categories': userchoice})

        products = self.cursor.fetchall()
        self.cursor.close()

        products_saved = []

        for element in products:
            products_saved.append(Product(element[1],
                                  element[2], None, None,
                                  None, None, element[0]))

        return products_saved
