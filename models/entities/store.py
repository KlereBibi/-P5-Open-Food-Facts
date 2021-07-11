"""module initializing store """

class Store:

    """ 
        Args : 
        - name (str) : name of store
        - id (int) : id with value None or database

        Attributs: 
        - attr1 (int) : value id in arguments
        - attr2 (str) : name of store (in arguments) 
        """

    def __init__(self, name, id=None):
    
        self.id = id
        self.name = name