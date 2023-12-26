from sqlalchemy.orm import sessionmaker

from mysql.MySQLDatabase import MySQLDatabase
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl
from product.service.ProductService import ProductService
from product.service.request.ProductRequestAdd import ProductRequestAdd


class ProductServiceImpl(ProductService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.engine = MySQLDatabase.getInstance().getMySQLEngine()
            cls.__instance.Session = sessionmaker(bind=cls.__instance.engine)
        return cls.__instance

    def __init__(self):
        print("TaskManageRepository 생성자 호출")
        self.__receiverTask = None
        self.__transmitterTask = None

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def productAdd(self, *args, **kwargs):

        request = ProductRequestAdd(**kwargs)
        print(f"request: {request}")
        response = ProductRepositoryImpl.getInstance().add(request.toProduct())
        print(f"response: {response}")
        return response
