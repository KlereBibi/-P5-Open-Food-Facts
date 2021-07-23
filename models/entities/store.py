"""module initializing store """

class Store:

    """ 
        Args : 
        - name (str) : name of store
        - id (int) : id with value None or database
        """

    def __init__(self, name, id=None):
    
        self.id = id
        self.name = name