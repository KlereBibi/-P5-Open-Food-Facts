
"""display module allowing interaction with the player"""

class Menu:

    """class menu to offer the different choices to the player
    return the choice (str) or False"""

    def main_user(self):

        """method showing the possible choices to the player"""

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

        """method requesting the name of the player's database
        return the choice (str)"""

        userchoice = input("merci d'inscrire le nom de votre base de donnée:\n")

        return userchoice

    def choice(self, message):

        print("Veuillez faire votre choix et inscrire le numéro correpondant: ")
        
        for element in message:
            print(element[0], ":", element[1])

        userchoice = input("")

        return userchoice


        
        