from sqlalchemy.orm import sessionmaker

from mysql.MySQLDatabase import MySQLDatabase
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl
from product.service.ProductService import ProductService
from product.service.request.ProductRequestAdd import ProductRequestAdd
from product.service.request.ProductRequestEdit import ProductRequestEdit
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



    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def productAdd(self, *args, **kwargs):
        # data = args[0]
        # request = ProductRequestAdd(*data)
        request = args[0]
        print(f"request: {request}")
        response = self.repository.add(request.toProduct())
        print(f"response: {response}")
        return response

    def productRemove(self, *args, **kwargs):
        request = args[0]
        #request = ProductRequestRemove(args[0])
        response = self.repository.removeByProductId(request)
        return response

    def productInfo(self, *args, **kwargs):
        #print(f"args: {args[0]}")
        #print(f"kwargs: {kwargs}")
        #request = ProductRequestFind(args[0])
        request = args[0]
        print(f"request: {request}")
        info = self.repository.findById(request)
        return info
        # response = ProductResponseInfo(info.getId(), info.getName(), info.getPrice(), info.getInfo())
        # return response

    def productList(self, *args, **kwargs):
        product_list = self.repository.findAllProducts()
        return product_list

    def productEdit(self, *args, **kwargs):
        # data = args[0]
        # request = ProductRequestEdit(*data)
        request = args[0]
        response = self.repository.edit(request)
        return response
