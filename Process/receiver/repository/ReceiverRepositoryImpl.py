import errno
from socket import socket
from time import sleep
import re

from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl
from receiver.repository.ReceiverRepository import ReceiverRepository
from transmitter.repository.TransmitterRepositoryImpl import TransmitterRepositoryImpl


class ReceiverRepositoryImpl(ReceiverRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("ReceiverRepositoryImpl 생성자 호출")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def receiveCommand(self, clientSocketObject, lock, receiveQueue):
        clientSocket = clientSocketObject.getSocket()
        print(f"receiver: is it exist -> {clientSocket}")

        while True:
            try:
                data = clientSocket.recv(1024)

                if not data:
                    clientSocket.closeSocket()
                    break

                decodedData = data.decode()
                print(f'수신된 정보: {decodedData}')
                responseObject = eval(decodedData)

                receiveQueue.put(responseObject)

            except socket.error as exception:
                if exception.errno == errno.EWOULDBLOCK:
                    pass

            finally:
                sleep(0.5)