from dataclasses import dataclass


@dataclass
class AccountDeleteResponse:
    __isSuccess: bool
    __message : str

    def __init__(self, isSuccess: bool, message: str = "계정 삭제 성공"):
        self.__isSuccess = isSuccess
        self.__message = message

    def __iter__(self):
        yield "__success", self.__isSuccess
        yield "__message", self.__message