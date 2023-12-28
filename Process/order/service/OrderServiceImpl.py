from sqlalchemy.orm import sessionmaker
from mysql.MySQLDatabase import MySQLDatabase
from order.repository.OrderRepositoryImpl import OrderRepositoryImpl
from order.entity.Order import ProductOrder
from order.service.OrderService import OrderService
from order.service.request.ProductBuyRequest import ProductBuyRequest
from order.service.response.ProductBuyResponse import productBuyResponse


class OrderServiceImpl(OrderService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.engine = MySQLDatabase.getInstance().getMySQLEngine()
            cls.__instance.Session = sessionmaker(bind=cls.__instance.engine)
            cls.__instance.repository = OrderRepositoryImpl.getInstance()
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

    def productBuy(self, *args, **kwargs):
        data = args[0]
        print(data)
        request = ProductBuyRequest(*data)
        if request.getAccountId() == -1:
            response = productBuyResponse(False, "로그인을 해주세요(주문 불가)")
            return response
        else:
            response = productBuyResponse(True, "주문이 완료되었습니다.")
            self.repository.add(request.toOrder())
            return response




