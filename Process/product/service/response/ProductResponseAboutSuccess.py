from dataclasses import dataclass


@dataclass
class ProductResponseAboutSuccess:
    __success: bool
    __message: str

    def __init__(self, success: bool, message: str):
        self.__success = success
        self.__message = message

    def __bool__(self):
        return self.__success
