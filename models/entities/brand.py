"""module initializing brand """

class Brand:

    """class to create a brand object"""

    def __init__(self, name, id=None):
    
        """ 
        Args : 
        - name (str) : name of brands 
        - id (int) : id with value None or database

        Attributs: 
        - attr1 (int) : value id in arguments
        - attr2 (str) : name of brands (in arguments)
        """

        self.id = id
        self.name = name