from dataclasses import dataclass


@dataclass
class ProductResponseInfo:
    __id:int
    __name:str
    __price:int
    __info:str

    def __init__(self, id:int, name:str, price:int, info:str):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__info = info

