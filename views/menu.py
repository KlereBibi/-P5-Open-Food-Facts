"""display module allowing interaction with the player"""
from views.display import Display


class Menu:

    """Class menu to offer the different choices to the player."""

    def main_user(self):

        """method showing the possible choices to the player.
        Detects with a condition if the user input matches
        one of the expected choices.
        return: str or False  """

        userchoice = input("Veuillez faire votre choix: \n \
            1/ Voir mes favoris\n \
            2/ Rechercher un substitut\n \
            3/ Réinitialiser la base de donnée \n \
            4/ Quitter le programme \n \
                Note: A tout moment, pour revenir au "
                           "menu principal appuyer sur q\n").lower()

        possibility = ("1", "2", "3", "4", "q")

        if userchoice.lower() in possibility:
            return userchoice.lower()
        else:
            return False

    def generic_choice(self, liste):

        """generic method allowing to make a choice
        among a list of object put in argument.
        With a condition, the user enters their choice
        which is returned or return to the main menu
        by pressing q which returns False.

        args:
        -message (list): contains the list of objects to select
        return: (str or False) choice utilisateur or False."""

        print("Veuillez faire votre choix"
              "et inscrire le numéro correpondant: ")

        for element in liste:
            print(element.id, ":", element.name)

        userchoice = input("").lower()

        if userchoice.lower() == "q":
            return False
        else:
            return userchoice.lower()

    def saved_substitute(self):

        """method asking the user if he wants to save his substitute.
        With a condition, returns the user's choice
        if it is in the list otherwise False

        return str or False """

        userchoice = input("Souhaitez vous enregistrer le résultat de votre recherche? \n \
        Pour oui tappez o pour non tappez n\n ").lower()

        possibility = ("o", "n", "q")

        if userchoice.lower() in possibility:
            return userchoice.lower()
        else:
            display = Display()
            display.retry()
            self.saved_substitute()
