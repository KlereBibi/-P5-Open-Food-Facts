from models.entities.substitute import Substitute
from models.managers.manager import Manager
from models.entities.product import Product
from models.entities.store import Store
from models.entities.brand import Brand

class SubstituteManager(Manager):

    def search_substitut(self, product):

        self.cursor.execute("SELECT ok.id, ok.name, ok.nutriscore, ok.url, b.name, s.name  FROM (SELECT DISTINCT p.id, p.name, p.nutriscore, p.url, count(*) as nb FROM products as p INNER JOIN categories_products as cp ON p.id = cp.id_products WHERE cp.id_categories IN (SELECT cp.id_categories FROM categories_products as cp WHERE id_products = %(id_products)s) AND NOT cp.id_products = %(id_products)s GROUP BY cp.id_products ORDER by nutriscore ASC) as ok INNER JOIN brands_products as bp ON ok.id = bp.id_products INNER JOIN stores_products as sp ON ok.id = sp.id_products INNER JOIN brands as b ON b.id = bp.id_brands INNER JOIN stores as s ON s.id = sp.id_stores WHERE nb = (SELECT MAX(nb) FROM (SELECT DISTINCT p.id, p.name, p.nutriscore, p.url, count(*) as nb FROM products as p INNER JOIN categories_products as cp ON p.id = cp.id_products WHERE cp.id_categories IN (SELECT cp.id_categories FROM categories_products as cp WHERE id_products = %(id_products)s) AND NOT cp.id_products = %(id_products)s GROUP BY cp.id_products ORDER by nutriscore ASC) as o) AND ok.nutriscore < %(nutriscore)s AND ok.id = (SELECT lo.id FROM (SELECT DISTINCT p.id, count(*) as nb FROM products as p INNER JOIN categories_products as cp ON p.id = cp.id_products WHERE cp.id_categories IN ( SELECT cp.id_categories FROM categories_products as cp WHERE id_products = 1134) AND NOT cp.id_products = 1134 GROUP BY cp.id_products ORDER by nutriscore ASC) as lo WHERE nb = (SELECT MAX(nb) FROM (SELECT DISTINCT p.id, count(*) as nb FROM products as p INNER JOIN categories_products as cp ON p.id = cp.id_products  WHERE cp.id_categories IN (SELECT cp.id_categories FROM categories_products as cp WHERE id_products = 1134 ) AND NOT cp.id_products = 1134 GROUP BY cp.id_products ORDER by nutriscore  ASC) as o ) AND ok.nutriscore <  'd' LIMIT 1);", {'id_products' : product.id, 'nutriscore': product.nutriscore})

        substitut = self.cursor.fetchall()

        

        if substitut:
            product_substitute = None
            for element in substitut:
                if product_substitute == None:
                    product_substitute = Product(element[1], element[2], None, element[3], Brand(element[4]), [Store(element[5])], element[0])   
                else:
                    store_list = []
                    for store in product_substitute.stores:#voir pour mieux 
                        store_list.append(store.name) #brands?
                    if element[5] not in store_list:
                        product_substitute.stores.append(Store(element[5], None))
                        
            return product_substitute
        else:
            return False


    def saved_substitut(self, o_substitute):

        tup_substitute = (o_substitute.id_products_origin, o_substitute.id_product_substitution)

        sql = "INSERT INTO substitute (id_product_origin, id_product_substitution) VALUES (%s, %s) ON DUPLICATE KEY UPDATE id_product_origin=id_product_origin"
        
        self.cursor.execute(sql, tup_substitute)

        self.connexion.commit()

        self.cursor.close()

    def all_substitute(self):

        self.cursor = self.connexion.cursor()

        self.cursor.execute("SELECT p.id, p.name, s.id, s.name FROM substitute INNER JOIN products as p ON substitute.id_product_origin = p.id INNER JOIN Products as s ON substitute.id_product_substitution = s.id")

        all_substitute = self.cursor.fetchall()

        if all_substitute:
            substitute_database = []

            for element in all_substitute:
                substitute_database.append((Product(element[1], None, None, None, None, None, element[0]), Product(element[3], None, None, None, None, None, element[2])))

            return substitute_database
        
        else:
            return False
            



