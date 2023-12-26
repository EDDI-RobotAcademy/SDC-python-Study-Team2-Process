import unittest

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from mysql.MySQLDatabase import MySQLDatabase
from product.entity.Product import Product
from product.repository.ProductRepository import ProductRepository
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl


class TestProductRepository(unittest.TestCase):
    def setUp(self):
        mysqlDatabase = MySQLDatabase.getInstance()
        mysqlDatabase.connect()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def testSave(self, _product):

        repository = ProductRepositoryImpl.getInstance()
        dbSession = sessionmaker(bind=repository.getInstance().engine)
        session = dbSession()

        try:
            session.add(_product)
            session.commit()

            print(f"product - id: {_product.getId()}")
            return _product

        except SQLAlchemyError as exception:
            session.rollback()
            print(f"DB 저장 중 에러 발생: {exception}")
            return None



    def testRemoveByProductId(self):
        _productId = 1
        repository = ProductRepositoryImpl.getInstance()
        dbSession = sessionmaker(bind=repository.engine)
        session = dbSession()

        product = session.query(Product).filter_by(_Product__id=_productId).first()
        if product:
            session.delete(product)
            session.commit()






    def testSaveProduct(self):
        repository = ProductRepositoryImpl.getInstance()
        product_data = {
            "name": "test_product",
            "price": 10000,
            "info": "test_info"
        }

        product = Product(**product_data)

        result = repository.add(product)

        self.assertTrue(result)

    def testDelete(self):
        repository = ProductRepositoryImpl.getInstance()
        product_data = {
            "name": "test_product",
            "price": 10000,
            "info": "test_info"
        }
        product = Product(**product_data)
        repository.add(product)

        result1 = repository.removeByProductId(1)
        result2 = repository.removeByProductId(2)
        result4 = repository.removeByProductId(7)

        self.assertIsNone(result1)
        self.assertIsNone(result2)
        self.assertIsNone(result4)


        # deletedAccount = repository.findByAccountId("delete_user")
        # self.assertIsNone(deletedAccount)

