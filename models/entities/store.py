"""module initializing store """


class Store:

    """class initializing store objects"""

    def __init__(self, name, id=None):

        """Args:
        -name (str): name of store
        -id (int): id with value None or database"""

        self.id = id
        self.name = name
