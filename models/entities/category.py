"""module initializing category """


class Category:

    """class to create a category object"""

    def __init__(self, name, id=None):

        """ Args:
        -name (str): name of category
        -id (int): id with value None or database"""

        self.id = id
        self.name = name
