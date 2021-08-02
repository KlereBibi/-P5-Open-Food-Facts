from views.menu import Menu
from views.display import Display
from models.managers.apimanager import ApiManager
from models.managers.datamanager import DataManager
from models.managers.productsmanager import ProductsManager
from models.managers.categoriesmanager import CategoriesManager
from models.managers.categoriesproductsmanager import CategoriesProductsManager

class Controller:

    def __init__(self):

        self.apimanager = ApiManager()
        self.datamanager = DataManager()
        self.message = Display()
        self.menu = Menu()
        self.categoriesmanager = CategoriesManager()
        self.categoriesproductsmanager = CategoriesProductsManager()
        self.productsmanager = ProductsManager()

    def ask_user(self):

        answer = self.menu.main_user()

        if answer:
            if answer == "3":
                self.choice_three()
            if answer == "2":
                self.choice_two()

    def choice_three(self):
        
        self.datamanager.delete_tables()
        self.message.display("La base de donnée a été réinitialisée")
        name_bdd = self.menu.name_bdd()
        self.message.display("Nous traitons votre demande, merci de patienter.")
        self.apimanager.save_data()
        self.message.display("La nouvelle base de donnée {} a été crée et complétée".format(name_bdd))
        self.ask_user()
        
    def choice_two(self):
        
        categories = self.categoriesmanager.search_categories()
        userchoice = self.menu.choice(categories)
        products = self.categoriesproductsmanager.search_product(userchoice)
        userchoice2 = self.menu.choice(products)
        
        