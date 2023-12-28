from dataclasses import dataclass

from product.entity.Product import Product


@dataclass
class ProductRequestEdit:
    __id: int
    __new_name: str
    __new_price: int
    __new_info: str

    def __init__(self, id: int, name: str, price: int, info: str):
        self.__id = id
        self.__new_name = name
        self.__new_price = price
        self.__new_info = info

    def getId(self):
        return self.__id

    def getNewName(self):
        return self.__new_name

    def getNewPrice(self):
        return self.__new_price

    def getNewInfo(self):
        return self.__new_info

    def toProduct(self):
        return Product(self.__new_name, self.__new_price, self.__new_info)