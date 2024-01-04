from dataclasses import dataclass


@dataclass
class ProductResponseInfo:
    __productId: int
    __productName: str
    __productPrice: int
    __productInfo: str

    def __init__(self, id:int, name:str, price:int, info:str):
        self.__productId = id
        self.__productName = name
        self.__productPrice = price
        self.__productInfo = info

    def __iter__(self):
        # 객체를 iterable로 만들기 위해 __iter__ 메서드를 정의
        yield "__productId", self.__productId
        yield "__productName", self.__productName
        yield "__productPrice", self.__productPrice
        yield "__productInfo", self.__productInfo

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price
