from models.managers.manager import Manager

class DataManager(Manager):
#"brands_products", "stores_products","categories_products, "brands", "stores", "categories","
    def delete_tables(self):

        tables = ( "brands_products", "stores_products","categories_products", "brands", "stores", "categories", "substitute", "products" )
        
        for element in tables:

            self.cursor = self.connexion.cursor()

            sql = "DROP TABLE {}".format(element)

            self.cursor.execute(sql)

            self.connexion.commit()

            print("supprimer")

            self.cursor.close()

        self.creat_table()

    def creat_table(self):

        self.cursor = self.connexion.cursor()

        sauvegarde = "C:\\Users\\klere\\Documents\\P5\\sauvegarde.sql"
        
        with open(sauvegarde) as infile:
            sqlrequests = infile.read().split(';')
            for sqlrequests in sqlrequests:
                if sqlrequests.strip():
                    self.cursor.execute(sqlrequests)



        #sql = "source sauvegarde"

        #for line in open("source C:\\Users\\klere\\Documents\\P5\\sauvegarde.sql","r"):
            #self.cursor.execute(line)

        #self.cursor.execute(sql)

        self.connexion.commit()

        self.cursor.close()

        self.cursor = self.connexion.cursor()

        sql = "SHOW TABLES"

        pouet = self.cursor.execute(sql)
        print (pouet)

        


            