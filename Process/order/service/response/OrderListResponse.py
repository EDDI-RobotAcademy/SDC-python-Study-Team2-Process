from dataclasses import dataclass

@dataclass
class OrderListResponse:
    __productId: int
    __productName: str
    __productPrice: int

    def __init__(self, id: int, name: str, price: int):
        self.__productId = id
        self.__productName = name
        self.__productPrice = price

    def __iter__(self):
        # 객체를 iterable로 만들기 위해 __iter__ 메서드를 정의
        yield "__productId", self.__productId
        yield "__productName", self.__productName
        yield "__productPrice", self.__productPrice

    def __dict__(self):
        return {
            "__productId": self.__productId,
            "__productName": self.__productName,
            "__productPrice": self.__productPrice
        }