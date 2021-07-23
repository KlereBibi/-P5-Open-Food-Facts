from views.menu import Menu
from models.managers.apimanager import ApiManager
from models.managers.datamanager import DataManager

class Controller:

    def ask_user(self):

        menu = Menu()
        answer = menu.main_user()
        if answer == "3":
            self.reinit_database()
        if answer: 
            name_bdd = menu.name_bdd()
            print("merci nous traitons votre demande")
            apimanager = ApiManager()
            apimanager.save_data()
            print("nouvelle base de donnée {} créer".format(name_bdd))
        else:
            self.ask_user()

    def reinit_database(self):

        datamanager = DataManager()
        datamanager.delete_tables()
        #change le nom 