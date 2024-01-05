from sqlalchemy.orm import sessionmaker

from order.entity.Order import ProductOrder
from order.repository.OrderRepository import OrderRepository
from mysql.MySQLDatabase import MySQLDatabase
from sqlalchemy.exc import SQLAlchemyError

from order.service.response.OrderRemoveResponse import OrderRemoveResponse


class OrderRepositoryImpl(OrderRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.engine = MySQLDatabase.getInstance().getMySQLEngine()
        return cls.__instance


    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def saveOrderInfo(self, orderInfo):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        try:
            session.add(orderInfo)
            session.commit()

            print(f"order - id: {orderInfo.getId()}")
            return orderInfo

        except SQLAlchemyError as exception:
            session.rollback()
            print(f"DB 저장 중 에러 발생: {exception}")
            return None

    def findAllProductIdByAccountId(self, accountId):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        accountIdList = session.query(ProductOrder).filter_by(_ProductOrder__accountId=accountId).all()
        productIdList = []
        for id in accountIdList:
            productIdList.append(id.getProductId())

        return productIdList

    def removeProductsByAccountId(self, sessionId):#, productId):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        products = session.query(ProductOrder).filter_by(_ProductOrder__accountId=sessionId).all()

        # products = session.query(ProductOrder).filter_by(_ProductOrder__accountId=sessionId,
        #                                                  _ProductOrder__productId=productId).all()

        if products:
            for product in products:
                session.delete(product)
                session.commit()
            response = OrderRemoveResponse(True, "주문 취소 완료")
        else:
            response = OrderRemoveResponse(False, "주문을 취소할 수 없습니다.")

        return response

    def removeOrderInfoByAccountId(self, sessionId):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        products = session.query(ProductOrder).filter_by(_ProductOrder__accountId=sessionId).all()
        print(f"products에 무슨 정보가 들었니?: {products}")

        if products:
            for product in products:
                session.delete(product)
            session.commit()
            return True

        return False

