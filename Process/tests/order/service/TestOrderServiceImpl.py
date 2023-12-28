import unittest

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from mysql.MySQLDatabase import MySQLDatabase
from order.repository.OrderRepositoryImpl import OrderRepositoryImpl
from order.entity.Order import ProductOrder



class TestProductRepository(unittest.TestCase):
    def setUp(self):
        mysqlDatabase = MySQLDatabase.getInstance()
        mysqlDatabase.connect()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def testBuy(self):

        repository = OrderRepositoryImpl.getInstance()
        dbSession = sessionmaker(bind=repository.engine)
        session = dbSession()

        _accountId = 12
        order_data = {
            "accountId": 12,
            "productId": 25
        }
        order = ProductOrder(**order_data)

        if _accountId == -1:
            print("주문 실패: 로그인 화면으로 이동")
            return False
        else:
            repository.save(order)
            return True