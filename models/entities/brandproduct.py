"""module initializing brandproduct """

class BrandProduct:

    """class to create a brandproduct object"""

    def __init__(self, id_product, id_brand):

        """ 
        Args : 
        - id_product (int) : id linked to a product
        - id_brand (int) : id linked to a brand

        Attributs: 
        - attr1 (int) : value id_product argument
        - attr2 (int) : value id_brand argument
        """

        self.id_products = id_product
        self.id_brands = id_brand