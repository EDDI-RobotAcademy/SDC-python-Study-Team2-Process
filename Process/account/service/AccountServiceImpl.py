from sqlalchemy.orm import Session

from account.entity.Account_Session import Account_Session
from account.repository.AccountRepositoryImpl import AccountRepositoryImpl
from account.repository.SessionRepositoryImpl import SessionRepositoryImpl
from account.service.AccountService import AccountService
from account.service.request.AccountDeleteRequest import AccountDeleteRequest
from account.service.request.AccountLoginRequest import AccountLoginRequest
from account.service.request.AccountLogoutRequest import AccountLogoutRequest
from account.service.request.AccountRegisterRequest import AccountRegisterRequest
from account.service.response.AccountDeleteResponse import AccountDeleteResponse
from account.service.response.AccountLoginResponse import AccountLoginResponse
from account.service.response.AccountLogoutResponse import AccountLogoutResponse
from account.service.response.AccountRegisterResponse import AccountRegisterResponse
from order.repository.OrderRepositoryImpl import OrderRepositoryImpl
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl


class AccountServiceImpl(AccountService):
    __instance = None

    def __new__(cls, repository):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.repository = repository
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__sessionRepository = SessionRepositoryImpl.getInstance()
            cls.__instance.__orderRepository = OrderRepositoryImpl.getInstance()
            cls.__instance.__productRepository = ProductRepositoryImpl.getInstance()

        return cls.__instance


    @classmethod
    def getInstance(cls, repository=None):
        if cls.__instance is None:
            cls.__instance = cls(repository)
        return cls.__instance

    def registerAccount(self, *args, **kwargs):
        print("registerAccount()")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")

        accountRegisterRequest = args[0]
        # print(f"cleanedElements: {cleanedElements}")
        #
        # # for i, element in enumerate(cleanedElements):
        # #     print(f"각각의 요소 {i + 1}: {element}")
        #
        # accountRegisterRequest = AccountRegisterRequest(*cleanedElements)
        print(f"accountRegisterRequest: {accountRegisterRequest}")
        if self.__accountRepository.findByAccountId(accountRegisterRequest.getAccountId()):
            return AccountRegisterResponse(False, "이미 존재하는 아이디입니다.")

        storedAccount = self.__accountRepository.save(accountRegisterRequest.toAccount())

        if storedAccount.getId() is not None:
            return AccountRegisterResponse(True)

        return AccountRegisterResponse(False, "알 수 없는 이유로 실패하였습니다.")

    def loginAccount(self, *args, **kwargs):
        print("loginAccount()")
        print(f"args: {args}")

        accountLoginRequest = args[0]
        # print(f"cleanedElements: {cleanedElements}")
        #
        # accountLoginRequest = AccountLoginRequest(*cleanedElements)
        print(f"accountLoginRequest id: {accountLoginRequest.getAccountId()}")
        foundAccount = self.__accountRepository.findByAccountId(accountLoginRequest.getAccountId())
        print(f"foundAccount: {foundAccount}")
        if foundAccount is None:
            return AccountLoginResponse(-1, "계정이 존재하지 않습니다.")

        if foundAccount.checkPassword(accountLoginRequest.getPassword()):
            # sessionRepository = SessionRepositoryImpl.getInstance()
            print(f"foundAccountId: {foundAccount.getId()}")
            accountSession = Account_Session(foundAccount.getId())
            print(f"accountSession: {accountSession}")
            # sessionRepository.save(accountSession)
            self.__sessionRepository.save(accountSession)

            return AccountLoginResponse(foundAccount.getId())
        return AccountLoginResponse(-1, "아이디와 비밀번호를 확인해 주세요.")

    def logoutAccount(self, *args, **kwargs):
        print("AccountService - logoutAccount()")
        print(f"args: {args}")

        accountLogoutRequest = args[0]
        # print(f"cleanedElements: {cleanedElements}")
        #
        # accountLogoutRequest = AccountLogoutRequest(*cleanedElements)
        foundAccount = self.__accountRepository.findById(accountLogoutRequest.getAccountSessionId())
        print(f"foundAccount: {foundAccount}")
        if foundAccount is None:
            return AccountLogoutResponse(False, "유효하지 않은 요청입니다.")

        self.__sessionRepository.deleteBySessionId(foundAccount.getId())

        return AccountLogoutResponse(True)

    def deleteAccount(self, *args, **kwargs):
        print("AccountService - deleteAccount()")

        accountDeleteRequest = args[0]

        # accountLoginRequest = AccountDeleteRequest(*cleanedElements)
        foundAccount = self.__accountRepository.findById(accountDeleteRequest.getAccountSessionId())
        print(f"foundAccount: {foundAccount}")
        if foundAccount is None:
            return AccountDeleteResponse(False, "유효하지 않은 계정입니다.")

        self.__orderRepository.removeOrderInfoByAccountId(foundAccount.getId())
        self.__sessionRepository.deleteBySessionId(foundAccount.getId())
        self.__accountRepository.deleteById(foundAccount.getId())
        self.__productRepository.removeProductAllBySessionId(foundAccount.getId())


        return AccountDeleteResponse(True)

    