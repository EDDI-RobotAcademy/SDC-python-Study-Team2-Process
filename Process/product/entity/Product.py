from dataclasses import dataclass
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

@dataclass
class Product(Base):
    __tablename__ = 'product'

    __productId: int = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __productName: str = Column(String, name="name")
    __productPrice: int = Column(Integer, name="price")
    __productInfo: str = Column(String, name="info")

    def __init__(self, name: str, price: int, info: str):
        self.__productName = name
        self.__productPrice = price
        self.__productInfo = info

    def getId(self):
        return self.__productId

    def getName(self):
        return self.__productName

    def getPrice(self):
        return self.__productPrice

    def getInfo(self):
        return self.__productInfo

    def editProduct(self, _newName: str, _newPrice: int, _newInfo: str) -> object:
        self.__productName = _newName
        self.__productPrice = _newPrice
        self.__productInfo = _newInfo


