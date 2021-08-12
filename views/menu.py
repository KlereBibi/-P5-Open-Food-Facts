
"""display module allowing interaction with the player"""

class Menu:

    """class menu to offer the different choices to the player
    return the choice (str) or False"""

    def main_user(self):

        """method showing the possible choices to the player"""

        userchoice = input("Veuillez faire votre choix :\n \
            1/ voir mes favoris\n \
            2/ rechercher un substitut\n \
            3/ réinitilisation de la base de donnée\n \
                Note: Pour revenir au menu principal appuyer sur q\n")

        liste = ("1", "2", "3", "q")
        
        if userchoice in liste:
            return userchoice
        else: 
            return False
    

    def name_bdd(self):

        """method requesting the name of the player's database
        return the choice (str)"""

        userchoice = input("Merci d'inscrire le nom de votre base de donnée:\n")

        return userchoice

    def choice(self, message):

        """method offering choices to the user among the lists
        args: message (list)
        return choice utilisateur or False 
        """
        print("Veuillez faire votre choix et inscrire le numéro correpondant: ")
        
        for element in message:
            print(element.id, ":", element.name)

        userchoice = input("")

        if userchoice == "q":
            return False
        else:
            return userchoice 
    
    def choice_saved_substitute(self):

        
        userchoice = input("Souhaitez vous enregistrer le résultat de votre recherche? \n Pour oui tappez o pour non tappez n\n ")

        liste = ("o", "n", "q")

        if userchoice in liste:
            return userchoice
        else:
            return False
    
    def return_main_menu(self):

        userchoice = input("Voulez vous revenir au menu principal? \n Appuyez sur o pour oui et n pour quitter le programme\n")

        liste = ("o", "n", "q")

        if userchoice in liste:
            return userchoice
        else:
            return False

    