from dataclasses import dataclass
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

@dataclass
class Product(Base):
    __tablename__ = 'product'

    __id: int = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __name: str = Column(String, name="name")
    __price: int = Column(Integer, name="price")
    __info: str = Column(String, name="info")

    def __init__(self, _name: str, _price: int, _info: str):
        self.__name = _name
        self.__price = _price
        self.__info = _info

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getInfo(self):
        return self.__info

    def editProduct(self, _newName: str, _newPrice: int, _newInfo: str):
        self.__name = _newName
        self.__price = _newPrice
        self.__info = _newInfo


