from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from mysql.MySQLDatabase import MySQLDatabase
from product.entity.Product import Product
from product.repository.ProductRepository import ProductRepository
from product.service.request.ProductRequestEdit import ProductRequestEdit
from product.service.request.ProductRequestFind import ProductRequestFind
from product.service.request.ProductRequestRemove import ProductRequestRemove
from product.service.response.ProductResponseAboutSuccess import ProductResponseAboutSuccess
from product.service.response.ProductResponseInfo import ProductResponseInfo
from product.service.response.ProductResponseList import ProductResponseList


class ProductRepositoryImpl(ProductRepository):
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

    def add(self, product):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()
        response = None

        try:
            session.add(product)
            session.commit()

            print(f"product - id: {product.getId()}")
            response = ProductResponseAboutSuccess(True, "저장 성공")

        except SQLAlchemyError as exception:
            session.rollback()
            print(f"DB 저장 중 에러 발생: {exception}")
            response = ProductResponseAboutSuccess(False, str(exception))

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

    def findById(self, request: ProductRequestFind):
        id = request.getProductId()
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        info = session.query(Product).filter_by(_Product__productId=id).first()
        if info:
            response = ProductResponseInfo(info.getId(), info.getName(), info.getPrice(), info.getInfo())
        else:
            response = ProductResponseAboutSuccess(False, "상품 번호를 확인 해 주세요")
        return response

    def edit(self, request: ProductRequestEdit):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        existingProduct = session.query(Product).filter_by(_Product__id=request.getId()).first()
        if existingProduct:
            if request.getNewPrice()<0:
                response = ProductResponseAboutSuccess(False, "유효하지 않은 가격입니다!")
            else:
                existingProduct.editProduct(request.getNewName(), request.getNewPrice(), request.getNewInfo())
                session.commit()
                response = ProductResponseAboutSuccess(True, "수정 성공!")
        else:
            response = ProductResponseAboutSuccess(False, "상품이 존재하지 않습니다")

        return response


    def findAllProducts(self):
        dbSession = sessionmaker(bind=ProductRepositoryImpl.getInstance().engine)
        session = dbSession()
        list = []
        for product in session.query(Product).all():
            response = ProductResponseList(product.getId(), product.getName(), product.getPrice())
            list.append(response)

        return list