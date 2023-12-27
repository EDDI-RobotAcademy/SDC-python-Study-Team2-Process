from sqlalchemy.orm import sessionmaker

from mysql.MySQLDatabase import MySQLDatabase
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl
from product.service.ProductService import ProductService
from product.service.request.ProductRequestAdd import ProductRequestAdd
from product.service.request.ProductRequestFind import ProductRequestFind
from product.service.request.ProductRequestRemove import ProductRequestRemove
from product.service.response.ProductResponseInfo import ProductResponseInfo


class ProductServiceImpl(ProductService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.engine = MySQLDatabase.getInstance().getMySQLEngine()
            cls.__instance.Session = sessionmaker(bind=cls.__instance.engine)
            cls.__instance.repository = ProductRepositoryImpl.getInstance()
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
        response = self.repository.add(request.toProduct())
        print(f"response: {response}")
        return response

    def productRemove(self, *args, **kwargs):
        request = ProductRequestRemove(args[0])
        response = self.repository.removeByProductId(request)
        return response


    def productFindById(self, *args, **kwargs):
        request = ProductRequestFind(args[0])
        print(f"request: {request}")
        info = self.repository.findById(request.getProductId())
        return info
        # response = ProductResponseInfo(info.getId(), info.getName(), info.getPrice(), info.getInfo())
        # return response
