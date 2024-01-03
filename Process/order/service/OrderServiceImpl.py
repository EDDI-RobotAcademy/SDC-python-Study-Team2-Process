from sqlalchemy.orm import sessionmaker
from mysql.MySQLDatabase import MySQLDatabase
from order.repository.OrderRepositoryImpl import OrderRepositoryImpl
from order.entity.Order import ProductOrder
from order.service.OrderService import OrderService
from order.service.request.OrderInfoRegisterRequest import OrderInfoRegisterRequest
from order.service.response.OrderInfoRegisterResponse import OrderInfoRegisterResponse
from order.service.response.OrderListResponse import OrderListResponse
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl
from product.service.ProductServiceImpl import ProductServiceImpl
from product.service.request.ProductRequestFind import ProductRequestFind


class OrderServiceImpl(OrderService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.engine = MySQLDatabase.getInstance().getMySQLEngine()
            cls.__instance.Session = sessionmaker(bind=cls.__instance.engine)
            cls.__instance.repository = OrderRepositoryImpl.getInstance()
            cls.__instance.productService = ProductServiceImpl.getInstance()
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


    def orderInfoRegister(self, *args, **kwargs):

        request = args[0]
        print(f"사용자 주문 요청 잘 들어 왔니?: {request}")

        if request.getSessionId() == -1:
            response = OrderInfoRegisterResponse(False, "로그인을 해주세요(주문 불가)")
            return response
        else:
            order_info = request.toOrder()
            saved_order = self.repository.saveOrderInfo(order_info)

            if saved_order:
                response = OrderInfoRegisterResponse(True, "주문이 완료되었습니다.")
            else:
                response = OrderInfoRegisterResponse(False, "주문을 저장하는데 문제 발생")
            return response


    def orderList(self, *args, **kwargs):

        request = args[0]
        print(f"주문 내역 요청 잘 들어 왔니?: {request}")

        sessionId = request.getSessionId()
        print(f"sessionId: {sessionId}")

        productIdList = self.repository.findAllProductIdByAccountId(sessionId)
        print(f"productIdList:{productIdList}")

        response = []
        for productId in productIdList:
            data = ProductServiceImpl.getInstance().productInfo(ProductRequestFind(productId))
            response.append(OrderListResponse(data.getName(), data.getPrice()))

        print(f"response: {response}")
        return response

    def orderRemove(self, *args, **kwqrgs):

        request = args[0]
        print(f"주문 취소 요청 잘 들어 왔니?: {request}")

        sessionId = request.getSessionId()
        print(f"주문 취소 sessionId: {sessionId}")

        productId = request.getProductId()

        print(f"주문 삭제 요청 잘 들어옴?: {request}")

        response = self.repository.removeProductsByAccountId(sessionId, productId)
        print(f"주문 취소 잘 됨?:{response}")

        return response

