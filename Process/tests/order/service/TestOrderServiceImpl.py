import unittest

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from mysql.MySQLDatabase import MySQLDatabase
from order.repository.OrderRepositoryImpl import OrderRepositoryImpl
from order.entity.Order import ProductOrder
from order.service.OrderServiceImpl import OrderServiceImpl
from order.service.request.OrderListRequest import OrderListRequest
from order.service.request.OrderRemoveRequest import OrderRemoveRequest
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl
from product.service.ProductServiceImpl import ProductServiceImpl
from product.service.request.ProductRequestFind import ProductRequestFind


class TestProductRepository(unittest.TestCase):
    def setUp(self):
        mysqlDatabase = MySQLDatabase.getInstance()
        mysqlDatabase.connect()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def testorderInfoRegister(self):

        repository = OrderRepositoryImpl.getInstance()

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
            repository.saveOrderInfo(order)
            return True


    def testOrderList(self):
        repository = OrderRepositoryImpl.getInstance()
        request = OrderListRequest(12)
        print(f"주문 내역 요청 잘 들어 왔니?: {request}")

        sessionId = request.getSessionId()
        print(f"sessionId: {sessionId}")

        result = repository.findAllProductIdByAccountId(sessionId)
        print(f"result: {result}")
        response = []
        for productId in result:

            response.append(ProductServiceImpl.getInstance().productInfo(ProductRequestFind(productId)))

        print(f"response: {response}")


    def testOrderDelete(self):
        repository = OrderRepositoryImpl.getInstance()
        request = OrderRemoveRequest(12, 5)
        sessionId = request.getSessionId()
        productId = request.getProductId()
        print(f"test 주문 삭제 요청 잘 들어옴?: {request}")

        response = repository.removeProductsByAccountId(sessionId, productId)
        print(f"test 주문 취소 잘 됨?:{response}")
