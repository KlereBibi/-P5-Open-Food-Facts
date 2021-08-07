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

    def substitute_ok(self, substitute):

        print("Le substitut correspondant à votre demande est : {}".format(substitute.name))

    def no_substitut(self):

        print("Désolé nous n'avons pas trouvé de substitut correspondant à la demande")