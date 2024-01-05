from account.repository.AccountRepositoryImpl import AccountRepositoryImpl
from account.repository.SessionRepositoryImpl import SessionRepositoryImpl
from account.service.response.AccountLogoutResponse import AccountLogoutResponse
from application.service.ApplicationService import ApplicationService
from mysql.MySQLDatabase import MySQLDatabase


class ApplicationServiceImpl(ApplicationService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.engine = MySQLDatabase.getInstance().getMySQLEngine()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__sessionRepository = SessionRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def applicationQuit(self, *args, **kwargs):
        request = args[0]
        message = "로그아웃이 불가능한 상태입니다. 일단 종료하세요~"
        try:
            foundAccount = self.__accountRepository.findById(request.getAccountSessionId())
            print(f"foundAccount: {foundAccount}")
            if self.__sessionRepository.deleteBySessionId(foundAccount.getId()):


                message = "로그아웃 되었습니다~ 종료하세요~"
        except Exception as e:
            print(f"exception: {e}")

        finally:
            return AccountLogoutResponse(True, message)
