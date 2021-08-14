"""module used to display the various messages intended for the user."""


class Display:

    """class comprising several methods called to display\
        the evolution of the process to the user"""

    def delete_tables(self):

        """method displaying that the tables were successfully\
            deleted when the database was reinitialized"""

        print("Les tables de la base de donnée ont été effacées")

    def wait(self):

        """method explaining to the user to wait\
            while the database is being filled"""

        print("Votre choix a été enregistré.\
            Le traitement des informations peut prendre quelques minutes,\
            merci de patienter")

    def finish(self, name_database):

        """method explaining that the database reset process is complete,\
            giving the database entry name entered by the player previously
        arg:
        name_database(str):name given to the database previously by the user"""

        print("La nouvelle base de donnée {} a été crée et \
            complétée".format(name_database))

    def retry(self):

        """method displaying an error message,\
             in particular during a false entry during an input"""

        print("La saisie est incorrect, merci de recommencer")

    def error_letters(self):

        """method displaying an error message,\
             in particular during a false entry during an input,\
                and that letters have been inscribed in place of a number"""

        print("La saisie est incorrect,\
             veuillez recommencer et saisir des chiffres")

    def substitute_ok(self, substitute):

        """method displaying the substitute found during searches,\
            giving the name of the substitute,the brand, \
            the different stores where it can be found \
            as well as the link to OpenFoodFact
        args:
        - substitute(class Product):containing the name of the substitute,\
        a list of store objects, a brands object and the url \
        corresponding to OpenFoodFact"""  #a confirmé

        print("Le substitut trouvé est {} de la marque {} que vous \
        pouvez trouver \
        chez".format(substitute.name, substitute.brands.name), end=" ")

        for element in substitute.stores:
            if element != substitute.stores[-1]:
                print(element.name, ",", end=" ")
            else:
                print(element.name, ".")

        print("Pour plus d'information,\
        veuillez trouver ci-joint \
        le lien vers OpenFoodFact {}.".format(substitute.url))

    def no_substitut(self):

        """method displaying the non possibility of finding a substitute"""

        print("Désolé nous n'avons pas trouvé \
            de substitut correspondant à la demande")

    def saved(self):

        """method validating the registration \
        of the substitute in the database"""

        print("Votre produit a bien été enregistré. ")

    def return_main(self):

        """method explaining the return to the main menu"""

        print("Retour au menu principal.")

    def all_substitute(self, liste_substitute):

        """method displaying the list of products \
            and their substitutes present in the database
        args:
        liste_substitute(liste):product object tuple liste \
        containing the names of the products associated with the substitute"""

        print("Voici le résultat de vos recherches:")

        for element in liste_substitute:
            print("-", element[0].name, "est remplacé \
            par", element[1].name, ".")

    def no_substitut_database(self):

        """method showing that the substitute table is empty"""

        print("La table des substituts est vide.")
