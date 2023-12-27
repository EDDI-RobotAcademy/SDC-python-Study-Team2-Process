from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from mysql.MySQLDatabase import MySQLDatabase
from product.entity.Product import Product
from product.repository.ProductRepository import ProductRepository
from product.service.request.ProductRequestRemove import ProductRequestRemove
from product.service.response.ProductResponseAboutSuccess import ProductResponseAboutSuccess
from product.service.response.ProductResponseList import ProductResponseList


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
        response = None

        try:
            session.add(product)
            session.commit()

            print(f"product - id: {product.getId()}")
            response = ProductResponseAboutSuccess(True, "")

        except SQLAlchemyError as exception:
            session.rollback()
            print(f"DB 저장 중 에러 발생: {exception}")
            response = ProductResponseAboutSuccess(True, str(exception))

        finally:
            return response

    def removeByProductId(self, request: ProductRequestRemove):
        _productId = request.getProductId()
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        product = session.query(Product).filter_by(_Product__id=_productId).first()
        if product:
            session.delete(product)
            session.commit()
            response = ProductResponseAboutSuccess(True, "삭제 완료")
        else:
            response = ProductResponseAboutSuccess(False, "올바르지 않은 상품 코드입니다")

        return response

    def findById(self, id):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        return session.query(Product).filter_by(_Product__id=id).first()

    def edit(self):
        pass

    def findAllProducts(self):
        dbSession = sessionmaker(bind=ProductRepositoryImpl.getInstance().engine)
        session = dbSession()
        list = []
        for product in session.query(Product).all():
            response = ProductResponseList(product.getId(), product.getName(), product.getPrice())
            list.append(response)

        return list

    def select(self):
        pass
