0
#encoding:utf-8
from entities.ApiManager import ApiManager
from entities.productmanager import ProductManager

apimanager = ApiManager()

listproduct = apimanager.creat_product()

productmanager = ProductManager()

productmanager.data_product(listproduct)







