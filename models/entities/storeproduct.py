"""module initializing storeproduct """


class StoreProduct:

    """class to create a storeproduct object"""

    def __init__(self, id_prod, id_sto):

        """ Args:
        -id_product (int): id linked to a product
        -id_store (int): id linked to a store

        Attributs:
        -attr1 (int): value id_product argument
        -attr2 (int): value id_store argument"""

        self.id_products = id_prod
        self.id_stores = id_sto
