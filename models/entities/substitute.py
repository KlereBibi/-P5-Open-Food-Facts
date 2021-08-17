"""module initiating substitute objects"""


class Substitute:

    """class initializing substitute objects"""

    def __init__(self, id_origin, id_substitution):

        """class constructor
        Args:
        id_origin(int): id product origin
        id_substitution(int): id product of substitution
        """

        self.id_products_origin = id_origin
        self.id_product_substitution = id_substitution
