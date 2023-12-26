from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from mysql.MySQLDatabase import MySQLDatabase
from product.entity.Product import Product
from product.repository.ProductRepository import ProductRepository


class ProductRepositoryImpl(ProductRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.engine = MySQLDatabase.getInstance().getMySQLEngine()
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

    def add(self, product):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        try:
            session.add(product)
            session.commit()

            print(f"product - id: {product.getId()}")
            return True

        except SQLAlchemyError as exception:
            session.rollback()
            print(f"DB 저장 중 에러 발생: {exception}")
            return False


    def removeByProductId(self, _productId):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        product = session.query(Product).filter_by(_Product__id=_productId).first()
        if product:
            session.delete(product)
            session.commit()
            print("삭제 완료")
            return True
        else:
            print("올바르지 않은 상품 코드")
            return False

    def edit(self):
        pass

    def list(self):
        pass

    def select(self):
        pass