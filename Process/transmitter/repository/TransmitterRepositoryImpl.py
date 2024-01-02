import multiprocessing
import socket
from datetime import datetime
from time import sleep

from transmitter.repository.TransmitterRepository import TransmitterRepository


class TransmitterRepositoryImpl(TransmitterRepository):
    __instance = None
    __transmitQueue = multiprocessing.Queue()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("TransmitterRepositoryImpl 생성자 호출")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def transmitCommand(self, clientSocket):
        while True:
            try:

                print(f"transmitter socket: {clientSocket}")
                print("transmitter: 응답 준비")
                response = self.__transmitQueue.get()
                if response is not None:
                    if response == 0:
                        print("transmitter: 종료~~~")
                        clientSocket.close()
                        break
                    else:
                        responseStr = str(response)
                        print(f"응답할 내용: {response}")
                        clientSocket.sendall(responseStr.encode())


            except (socket.error, BrokenPipeError) as exception:
                print(f"사용자 연결 종료: {exception}")
                return None

            except socket.error as exception:
                print(f"전송 중 에러 발생: str{exception}")

            except Exception as exception:
                print(f"원인을 알 수 없는 에러가 발생하였습니다: {exception}")

            finally:
                sleep(0.5)

    def getTransmitQueue(self):
        return self.__transmitQueue