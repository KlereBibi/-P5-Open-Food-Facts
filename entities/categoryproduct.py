from categoryproductmanager import CategoryProductManager

class CategoryProduct:

    def liaison_id(self, listeproductsansid):

        #initialisation de la class CategoryProductManager
        catepromanager = CategoryProductManager()
        #appel de ma méthode récupérant les données dans la base avec id 
        liste_tup_id_catego = catepromanager.take_id_catego()
        #récupération des id des products
        liste_id_prod = catepromanager.take_id_product()
        #création de la liste contenant les tuples de (id de l'objet et nom de catégorie)
        liste_product_catego_id = []

        #boucle for permettant de remplir les id des objets products
        for product in listeproductsansid:
            for tuple in liste_id_prod:
                if product.name == tuple[1]:
                    product.id = tuple[0]
                    #boucle for pour enregistrer les id du products au catégories correspondantes de la liste
                    for element in product.categories:
                        liste_product_catego_id.append((product.id, element.name))
   
        tup_liaison_id = []

        #comparaison des deux listes et association des 2 id si indentique
        for element in liste_product_catego_id:
            for each in liste_tup_id_catego:
                if element[1] == each[1]:
                    tup_liaison_id.append((element[0], each[0]))

        #appel de la méthode permettant d'enregistrer les liasons
        catepromanager.save_liaison(tup_liaison_id)

            
                


            

