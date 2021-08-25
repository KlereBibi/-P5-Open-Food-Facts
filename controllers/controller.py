"""module leading code coordination"""

from views.menu import Menu
from views.display import Display
from models.entities.substitute import Substitute
from models.managers.apimanager import ApiManager
from models.managers.datamanager import DataManager
from models.managers.productsmanager import ProductsManager
from models.managers.categoriesmanager import CategoriesManager
from models.managers.substitutemanager import SubstituteManager


class Controller:

    """class used to retrieve information,
    process it according to the parameters requested by the view
    and then return the data to the view for display."""

    def __init__(self):

        """initialization in variables of the different
        classes activated by the controller"""

        self.datamanager = DataManager()
        self.display = Display()
        self.menu = Menu()
        self.substitutemanager = SubstituteManager()

    def chek_database(self):

        """method allowing to know by launching
        the script if the database is empty"""

        database_empty = self.datamanager.search_tables()
        if database_empty:
            self.display.database_empty()
            self.reboot_database()
            self.ask_user()
        else:
            self.ask_user()

    def ask_user(self):

        """method calling the view function to offer the main menu
        to the user then call the corresponding method"""

        answer = self.menu.main_user()

        if answer:

            if answer == "1":

                all_substitute = self.substitutemanager.all_substitute()
                if all_substitute:
                    self.display.all_substitute(all_substitute)
                    self.ask_user()
                else:
                    self.display.no_substitut_database()
                    self.ask_user()

            if answer == "2":
                self.choice_categories()

            if answer == "3":
                self.reboot_database()

            if answer == "q":
                self.ask_user()

        else:
            self.display.retry()
            self.ask_user()

    def reboot_database(self):

        """method calling another manager method allowing
        to reinitialize the information contained in the database
        by deleting the tables and their contents then by recreating them."""

        apimanager = ApiManager()
        self.datamanager.delete_tables()
        self.display.delete_tables()
        self.display.wait()
        apimanager.save_data()
        self.display.finish()
        self.ask_user()

    def choice_categories(self):

        """method offering the user several choices of categories"""

        categoriesmanager = CategoriesManager()
        categories = categoriesmanager.search_categories()

        user_category = self.menu.generic_choice(categories)

        if user_category:

            try:
                selected_categories = [categorie for categorie in categories
                                       if categorie.id == int(user_category)]
                if selected_categories:
                    self.choice_product(user_category)
                else:
                    self.display.retry()
                    self.choice_categories()
            except ValueError:
                self.display.error_letters()
                self.choice_categories()

        else:

            self.ask_user()

    def choice_product(self, user_category):

        """method calling other methods to offer the user several choices
        of products in the selected categories"""

        productsmanager = ProductsManager()
        products = productsmanager.search_products(user_category)
        user_product = self.menu.generic_choice(products)

        for element in products:
            if str(element.id) == user_product:
                product = element

        if user_product:

            try:
                selected_products = [product for product in products
                                     if product.id == int(user_product)]
                if selected_products:
                    self.substitute(product)
                    self.display.saved()
                    self.ask_user()
                else:
                    self.display.retry()
                    self.choice_product(user_category)
            except ValueError:
                self.display.error_letters()
                self.choice_product(user_category)
        else:

            self.ask_user()

    def substitute(self, product):

        """method calling other methods to find
        the substitute corresponding to the selected product"""

        substitute = self.substitutemanager.search_substitut(product)

        if substitute:
            self.display.substitute_ok(substitute)
            userchoice = self.menu.saved_substitute()

            if userchoice == "o":
                o_substitute = Substitute(product.id, substitute.id)
                self.substitutemanager.saved_substitut(o_substitute)
                self.display.saved()
                self.display.return_main()
                self.ask_user()
            if userchoice == "n":
                self.ask_user()
            if userchoice == "q":
                self.ask_user()

        else:
            self.display.no_substitut()
            self.ask_user()
