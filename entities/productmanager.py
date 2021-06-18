from category import Category
from categorymanager import CategoryManager
from manager import Manager
import mysql.connector

class ProductManager(Manager):

    def save_product_tup(self, liste):
        
        """ méthode pour transformer les objets products en tuples. 
        initialisation de l'objet category manager pour ajouter dans la liste du constructeur les tuples des categories
        appel de la fonction pour enregistrer les catégories 
        return la liste de tuples """

        #creation de liste de tuple
        list_tup_catego = []
        list_tup_prod = []
        categomanager = CategoryManager()
        #transformation en tuples
        for element in liste: 
            list_tup_prod.append((None, element.name, element.nutriscore, element.url))
            for catego in element.categories:
                list_tup_catego.append((None, catego.name))
                #A REVOIR !!!!!!! une requête pour chaque product ou une requête global?
        
        categomanager.save_catego_table(list_tup_catego)

        return list_tup_prod

    def save_in_table(self, liste):

        """méthode enregistrant la liste des produits dans la base off en appelant la class mère"""

        products_list = self.save_product_tup(liste)
       
        
        sql = "INSERT INTO products (id, name, nutriscore, url) VALUES (%s, %s, %s, %s)"

        value = products_list

        self.cur.executemany(sql, value)

        self.connexion_off.commit()
        
        #afficher le nombre de lignes insérées
        print(self.cur.rowcount, "ligne insérée.")


  