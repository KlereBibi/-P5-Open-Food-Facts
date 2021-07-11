"""module initializing categoryproduct """

class CategoryProduct:

    """class to create a categoryproduct object"""

    def __init__(self, id_prod, id_cat):

        """ 
        Args : 
        - id_product (int) : id linked to a product
        - id_category (int) : id linked to a category

        Attributs: 
        - attr1 (int) : value id_product argument
        - attr2 (int) : value id_category argument
        """

        self.id_product = id_product

        self.id_category = id_category