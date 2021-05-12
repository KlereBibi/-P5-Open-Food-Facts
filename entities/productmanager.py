
class ProductManager:

    def search_all_categories(self, products):

        mysecondlist = []
        category = []
        mylist = []

        for element in products: #la liste des products 
            mylist.append(element["categories"])

        for element in mylist: #séparer les chaines de caractère, sort sous forme de listes
            a = element.split(',')
            mysecondlist.append(a)

        for element in mysecondlist: # itérer sur chaque élement pour l'ajouter dans la liste des catégories sans doublon
            for i in element:
                if i not in category:
                    category.append(i)

        print(category)
        return category

    def creat_category(self, products):

        for element in self.search_all_categories(products): #création de l'objet
            print(type(element))
            element = type("", (), {})
            print(type(element))
        