from categoryproductmanager import CategoryProductManager

class CategoryProduct:

    def liaison_id(self, listeproductsansid):

        catepromanager = CategoryProductManager()
        liste_tup_id_catego = catepromanager.take_id_catego()
        liste_id_prod = catepromanager.take_id_product()

        liste_product_catego_id = []

        for product in listeproductsansid:
            for tuple in liste_id_prod:
                if product.name == tuple[1]:
                    product.id = tuple[0]
                    for element in product.categories:
                        liste_product_catego_id.append((product.id, element.name))
   
        tup_liaison_id = []

        for element in liste_product_catego_id:
            for each in liste_tup_id_catego:
                if element[1] == each[1]:
                    tup_liaison_id.append((element[0], each[0]))

        catepromanager.save_liaison(tup_liaison_id)

            
                


            

