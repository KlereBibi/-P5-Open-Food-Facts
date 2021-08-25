"""module allowing to communicate with the database
and to interact with the substitute table"""

from models.managers.manager import Manager
from models.entities.product import Product
from models.entities.store import Store
from models.entities.brand import Brand


class SubstituteManager(Manager):

    """child class inheriting from the manager class containing
    the connection to the database and opening a new cursor.
        Args:
    Manager (class): connexion to the database"""

    def search_substitut(self, product):

        """method containing an sql query allowing
        to search the database for a substitute
        Args:
        -product (object product):
        contains the product substituted
        Returns:
        product_substitute (product object): returns the product
        with a better nutriscore and the maximum of category.
        False: if the result of the query is empty"""

        cursor = self.connexion.cursor()
        cursor.execute("SELECT \
            ok.id, ok.name, ok.nutriscore, ok.url, b.name, s.name \
            FROM \
                (SELECT DISTINCT p.id, p.name, p.nutriscore, p.url, \
                    count(*) as nb \
                FROM products as p \
                INNER JOIN categories_products as cp \
                ON p.id = cp.id_products \
                WHERE cp.id_categories \
                IN \
                    (SELECT cp.id_categories \
                    FROM categories_products as cp \
                    WHERE id_products = %(id_products)s) \
                AND NOT cp.id_products = %(id_products)s \
                GROUP BY cp.id_products \
                ORDER by nutriscore ASC) as ok \
            INNER JOIN brands_products as bp \
            ON ok.id = bp.id_products \
            INNER JOIN stores_products as sp \
            ON ok.id = sp.id_products \
            INNER JOIN brands as b \
            ON b.id = bp.id_brands \
            INNER JOIN stores as s \
            ON s.id = sp.id_stores \
            WHERE nb = \
                (SELECT MAX(nb) \
                FROM \
                    (SELECT DISTINCT p.id, p.name, p.nutriscore, p.url, \
                        count(*) as nb \
                    FROM products as p \
                    INNER JOIN categories_products as cp \
                    ON p.id = cp.id_products \
                    WHERE cp.id_categories \
                    IN \
                        (SELECT cp.id_categories \
                        FROM categories_products as cp \
                        WHERE id_products = %(id_products)s) \
                        AND NOT cp.id_products = %(id_products)s \
                        GROUP BY cp.id_products \
                        ORDER by nutriscore ASC) as o) \
            AND ok.nutriscore < %(nutriscore)s \
            AND ok.id = \
                (SELECT lo.id \
                FROM \
                    (SELECT DISTINCT p.id, count(*) as nb \
                    FROM products as p \
                    INNER JOIN categories_products as cp \
                    ON p.id = cp.id_products \
                    WHERE cp.id_categories \
                    IN \
                        (SELECT cp.id_categories \
                        FROM categories_products as cp \
                        WHERE id_products = %(id_products)s) \
                    AND NOT cp.id_products =  %(id_products)s \
                    GROUP BY cp.id_products \
                    ORDER by nutriscore ASC) as lo \
                WHERE nb = \
                    (SELECT MAX(nb) \
                    FROM \
                        (SELECT DISTINCT p.id, count(*) as nb \
                        FROM products as p \
                        INNER JOIN categories_products as cp \
                        ON p.id = cp.id_products \
                        WHERE cp.id_categories \
                        IN \
                            (SELECT cp.id_categories \
                            FROM categories_products as cp \
                            WHERE id_products = %(id_products)s ) \
                        AND NOT cp.id_products = %(id_products)s \
                        GROUP BY cp.id_products \
                        ORDER by nutriscore  ASC) as o ) \
                AND ok.nutriscore <  'd' LIMIT 1);",
                       {'id_products': product.id,
                        'nutriscore': product.nutriscore})

        substitut = cursor.fetchall()
        super().end_request(cursor)

        if substitut:
            product_substitute = None
            for element in substitut:
                if product_substitute is None:
                    product_substitute = \
                        Product(element[1], element[2], None, element[3],
                                Brand(element[4]), [Store(element[5])],
                                element[0])
                else:
                    store_list = []
                    for store in product_substitute.stores:
                        store_list.append(store.name)
                    if element[5] not in store_list:
                        product_substitute.stores.append(Store(element[5],
                                                               None))

            return product_substitute
        else:
            return False

    def saved_substitut(self, o_substitute):

        """method recording in the substitute table
        the substitute corresponding to the requested product
        Args:
        - o_substitut(object): contains id product and substitut"""

        cursor = self.connexion.cursor()
        tup_substitute = (o_substitute.id_products_origin,
                          o_substitute.id_product_substitution)

        sql = "INSERT INTO substitute (id_product_origin, id_product_substitution) \
            VALUES (%s, %s) \
            ON DUPLICATE \
            KEY UPDATE id_product_origin=id_product_origin"

        cursor.execute(sql, tup_substitute)
        super().end_request(cursor)

    def all_substitute(self):

        """method requesting all the elements present in the substitute table.
        return:
        substitute_database(liste): product and substitut in database
        False(condition): if no element in the request"""

        cursor = self.connexion.cursor()
        cursor.execute("SELECT p.id, p.name, s.id, s.name \
                            FROM substitute \
                            INNER JOIN products as p \
                            ON substitute.id_product_origin = p.id \
                            INNER JOIN Products as s \
                            ON substitute.id_product_substitution = s.id")

        all_substitute = cursor.fetchall()
        super().end_request(cursor)

        if all_substitute:
            substitute_database = []

            for element in all_substitute:
                substitute_database. \
                    append(
                           (Product(element[1],
                            None, None, None, None, None, element[0]),
                            Product(element[3], None, None,
                            None, None, None, element[2])))

            return substitute_database

        else:
            return False
