
from sqlalchemy.orm import sessionmaker

from account.entity.Account_Session import Account_Session
from account.repository.SessionRepository import SessionRepository
from mysql.MySQLDatabase import MySQLDatabase
from sqlalchemy.exc import SQLAlchemyError


class SessionRepositoryImpl(SessionRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.engine = MySQLDatabase.getInstance().getMySQLEngine()
        return cls.__instance

    def __init__(self):
        print("SessionRepositoryImpl 생성자 호출")
        self.__receiverTask = None
        self.__transmitterTask = None

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance


    def save(self, accountSession):
        print("SessionRepositoryImpl: save()")
        print(f"accountSession: {accountSession}")
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        try:
            print("1")
            session.add(accountSession)
            print("2")
            session.commit()
            print("3")

            print(f"accountSession - id: {accountSession.getSessionId()}")
            return accountSession

        except SQLAlchemyError as exception:
            session.rollback()
            print(f"DB 저장 중 에러 발생: {exception}")
            return None

    def findById(self, id):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        return session.query(Account_Session).filter_by(_Session__id=id).first()

    def findBySessionId(self, sessionId):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        return session.query(Account_Session).filter_by(_Session__sessionId=sessionId).first()

    def deleteBySessionId(self, sessionId):
        print("deleteBySessionId 호출: {sessionId}")
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()
        print(1)
        accountSession = session.query(Account_Session).filter_by(_Account_Session__sessionId=sessionId).first()
        print(2)
        if accountSession:
            session.delete(accountSession)
            session.commit()

