#encoding:utf-8
from entities.ApiManager import ApiManager
from entities.productmanager import ProductManager

apimanager = ApiManager()
products = apimanager.search_products()
productmanager = ProductManager()
category = productmanager.creat_category(products) 




