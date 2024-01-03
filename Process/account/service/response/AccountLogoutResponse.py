from dataclasses import dataclass


@dataclass
class AccountLogoutResponse:
    __isSuccess: bool
    __message: str

    def __init__(self, isSuccess: bool, message: str = "로그아웃 성공"):
        self.__isSuccess = isSuccess
        self.__message = message

    def __iter__(self):
        yield "isSuccess", self.__isSuccess
        yield "message", self.__message