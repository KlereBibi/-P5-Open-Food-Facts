"""module initializing categoryproduct """


class CategoryProduct:

    """class to create a categoryproduct object"""

    def __init__(self, id_product, id_category):

        """ Args:
        - id_product (int) : id linked to a product
        - id_category (int) : id linked to a category"""

        self.id_product = id_product
        self.id_category = id_category
