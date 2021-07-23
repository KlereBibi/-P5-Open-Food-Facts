class Menu:

    def main_user(self):

        userchoice = input("Veuillez faire votre choix :\n \
            1/ voir mes favoris\n \
            2/ rechercher un substitut\n \
            3/ réinitilisation de la base de donnée\n")

        liste = ("1", "2", "3")
        
        if userchoice in liste:
            return userchoice
        else: 
            return False
    

    def name_bdd(self):

        userchoice = input("merci d'inscrire le nom de votre base de donnée:\n")

        return userchoice
        
