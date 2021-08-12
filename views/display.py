class Display:

    def delete_tables(self):

        print("Les tables de la base de donnée ont été effacées")

    def wait(self):

        print("Votre choix a été enregistré. Le traitement des informations peut prendre quelques minutes, merci de patienter")

    def finish(self, name_database):

        print("La nouvelle base de donnée {} a été crée et complétée".format(name_database))

    def retry(self):

        print("La saisie est incorrect, merci de recommencer")

    def error_letters(self):

        print("La saisie est incorrect, veuillez recommencer et saisir des chiffres")

    def substitute_ok(self, substitute, brands, stores ):

        name_brands = []
        for element in brands:
            name_brands.append(element.name)

        name_stores = []
        for element in stores:
            name_stores.append(element.name)

        print("Le substitut correspondant à votre demande est {}".format(substitute.name), "", end='')

        print("de la marque ", end='')

        for element in name_brands:
            print(element, "", end='')
        
        print("que vous prouvez trouver chez ", end='')

        for element in name_stores:
            if element != name_stores[-1]:
                print(element, ",", "", end='')
            else:
                print(element, ".")
        
    def no_substitut(self):

        print("Désolé nous n'avons pas trouvé de substitut correspondant à la demande")

    def saved(self):

        print("Votre produit a bien été enregistré. ")

    def return_main(self):

        print("Retour au menu principal.")

    def all_substitute(self, liste_substitute):

        print("Voici le résultat de vos recherches:")

        for element in liste_substitute:
            print("-", element[0].name, "est remplacé par", element[1].name,".")
    
    def no_substitut_database(self):

        print("La table des substituts est vide.")

    
            