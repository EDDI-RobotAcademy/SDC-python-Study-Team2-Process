from sqlalchemy.orm import sessionmaker
from mysql.MySQLDatabase import MySQLDatabase
from order.repository.OrderRepositoryImpl import OrderRepositoryImpl
from order.entity.Order import ProductOrder
from order.service.OrderService import OrderService
from order.service.request.OrderInfoRegisterRequest import OrderInfoRegisterRequest
from order.service.response.OrderInfoRegisterResponse import OrderInfoRegisterResponse


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

    #def productBuy(self, *args, **kwargs):
    #    data = args[0]
    #    request = ProductBuyRequest(*data)
    #    if request.getAccountId() == -1:
    #        response = productBuyResponse(False, "로그인을 해주세요(주문 불가)")
    #        return response
    #    else:
    #        response = productBuyResponse(True, "주문이 완료되었습니다.")
    #        self.repository.add(request.toOrder())
    #        return response

    def orderInfoRegister(self, *args, **kwargs):
        #data = args[0]
        #print(f"아이디들 잘 들어 왔니?: {data}")
        #request = ProductBuyRequest(*data)
        request = args[0]

        if request.getAccountId() == -1:
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


