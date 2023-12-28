from dataclasses import dataclass

#from account.entity.Account import Account
from account.entity.Account_Session import Account_Session


@dataclass
class SessionLoginRequest:
    __accountId: str
    __password: str

    def toSession(self):
        return Account_Session(self.__accountId, self.__password)

    def __init__(self, accountId=None, password=None, **kwargs):
        if accountId is not None and password is not None:
            self.__accountId = accountId
            self.__password = password
        elif "__accountId" in kwargs and "__password" in kwargs:
            self.__accountId = kwargs["__accountId"]
            self.__password = kwargs["__password"]

    @classmethod
    def createFromTuple(cls, inputTuple):
        return cls(*inputTuple)

    def getAccountId(self):
        return self.__accountId

    def getPassword(self):
        return self.__password