import unittest

from mysql.MySQLDatabase import MySQLDatabase
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl
from product.service.ProductServiceImpl import ProductServiceImpl
from product.service.request.ProductRequestAdd import ProductRequestAdd


class TestProductServiceImpl(unittest.TestCase):
    def setUp(self):
        mysqlDatabase = MySQLDatabase.getInstance()
        mysqlDatabase.connect()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def testProductAdd(self):
        repository = ProductRepositoryImpl.getInstance()
        service = ProductServiceImpl.getInstance()
        product_data = {
            "name": "testProduct",
            "price": 33333,
            "info": "testInfo"
        }

        response = service.productAdd(**product_data)

        # response = ProductRepositoryImpl.getInstance().add(request.toProduct())
        print(f"response: {response}")
        self.assertTrue(response)

    def testDelete(self):
        repository = ProductRepositoryImpl.getInstance()
        service = ProductServiceImpl.getInstance()
        product_id = 5
        result = service.productRemove(product_id)
        print(f"result: {result}")

    def testFind(self):
        repository = ProductRepositoryImpl.getInstance()
        service = ProductServiceImpl.getInstance()
        id = 24
        result = service.productInfo(id)
        print(f"result: {result}")
        self.assertIsNotNone(result)

    def testFindAll(self):
        repository = ProductRepositoryImpl.getInstance()
        service = ProductServiceImpl.getInstance()
        result = service.productList()
        print(f"result: {result}")
        self.assertIsNotNone(result)

    def testEdit(self):
        editData = {
            "id": 25,
            "name": "editName",
            "price": 8888,
            "info": "editInfo"
        }
        service = ProductServiceImpl.getInstance()
        result = service.productEdit(**editData)
        self.assertTrue(result)
