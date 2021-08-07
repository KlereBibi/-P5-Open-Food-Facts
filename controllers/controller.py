"""module leading code coordination"""


from views.menu import Menu

from views.display import Display

from models.managers.apimanager import ApiManager

from models.managers.datamanager import DataManager

from models.managers.productsmanager import ProductsManager

from models.managers.categoriesmanager import CategoriesManager

from models.managers.categoriesproductsmanager import CategoriesProductsManager


class Controller:


    """class used to retrieve information, process it according to the parameters requested by the view and then return the data to the view for display."""


    def __init__(self):


        """initialization in variables of the different classes activated by the controller"""


        self.apimanager = ApiManager()

        self.datamanager = DataManager()

        self.message = Display()

        self.menu = Menu()

        self.categoriesmanager = CategoriesManager()

        self.categoriesproductsmanager = CategoriesProductsManager()

        self.productsmanager = ProductsManager()


    def ask_user(self):


        """method calling the view function to offer the main menu to the user then call the corresponding method"""


        answer = self.menu.main_user()


        if answer:

            if answer == "3":

                self.reboot_database()

            if answer == "2":
                self.choice_categories()

            if answer == "q":

                self.ask_user()

        else: 

            self.message.retry()

            self.ask_user()


    def reboot_database(self):


        """method calling another manager method allowing to reinitialize the information contained in the database by deleting the tables and their contents then by recreating them"""


        self.datamanager.delete_tables()

        self.message.delete_tables()

        name_bdd = self.menu.name_bdd()

        self.message.wait()

        self.apimanager.save_data()

        self.message.finish(name_bdd)

        self.ask_user()
        

    def choice_categories(self):


        categories = self.categoriesmanager.search_categories()

        user_category = self.menu.choice(categories)

        if user_category:

            try:

                selected_categories = [categorie for categorie in categories if categorie.id == int(user_category)]

                if selected_categories:

                    self.choice_product(user_category)

                else:

                    self.message.retry()
                    self.choice_categories()


            except ValueError:
                self.message.error_letters()
                self.choice_categories()

        else: 

            self.ask_user()


    def choice_product(self, user_category):
        
        #MENTORAT : est ce au bon endroit (categories_products_manager)

        products = self.categoriesproductsmanager.search_products(user_category)

        user_product = self.menu.choice(products)

        for element in products:
            if str(element.id) == user_product:
                product = element

        if user_product:

            try:

                selected_products = [product for product in products if product.id == int(user_product)]

                if selected_products:
                    
                    self.substitut(product)
                
                else:

                    self.message.retry()

                    products = self.choice_productscategories

                    userchoice = self.menu.choice(products)

            except ValueError:
                self.message.error_letters()
                self.choice_productscategories(userchoice)

        else:

            self.ask_user()

    def substitut(self, product):

        substitute = self.productsmanager.search_substitut(product)

        if substitute:
            self.message.substitute_ok(substitute)

            userchoice = self.menu.choice_saved_substitute()

            if userchoice: 

                if userchoice == "o":
                    pass
                if userchoice == "n":
                    pass 
                if userchoice == "q":
                    self.ask_user()

            else:

                self.message.retry()

        else: 
            self.message.no_substitut()

       