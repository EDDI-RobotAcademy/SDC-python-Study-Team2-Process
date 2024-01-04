import errno
import json
from socket import socket
from time import sleep

from account.repository.SessionRepositoryImpl import SessionRepositoryImpl
from account.service.response.AccountLoginResponse import AccountLoginResponse
from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl
from receiver.repository.ReceiverRepository import ReceiverRepository
from request_generator.service.RequestGeneratorServiceImpl import RequestGeneratorServiceImpl
from transmitter.repository.TransmitterRepositoryImpl import TransmitterRepositoryImpl

import re

from utility.SocketSessionRepository import SocketSessionRepository
from utility.converter.ConvertToTransmitMessage import ConvertToTransmitMessage


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

    def receiveCommand(self, clientSocket):
        transmitterRepository = TransmitterRepositoryImpl.getInstance()
        transmitQueue = transmitterRepository.getTransmitQueue()

        customProtocolRepository = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()

        converter = ConvertToTransmitMessage.getInstance()

        while True:
            try:
                receivedRequest = clientSocket.recv(2048)
                if not receivedRequest:
                    print("ReceiverRepositoryImpl: 소켓종료")
                    # transmitter에게 접속이 종료되었다고 알려야합니다.
                    transmitQueue.put(0)
                    if clientSocket in SocketSessionRepository.getSocketSession():

                        SessionRepositoryImpl.getInstance().deleteBySessionId(SocketSessionRepository.getSocketSession()[clientSocket])
                        SocketSessionRepository.deleteSocketSession(clientSocket)

                    clientSocket.close()
                    break
                receivedForm = json.loads(receivedRequest)

                protocolNumber = receivedForm["protocol"]

                receivedRequestForm = receivedForm["data"]
                print(f"receivedRequestForm: {receivedRequestForm}")

                requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
                requestForm = requestGenerator(receivedRequestForm)

                # decodedRequest = receivedRequest.decode('utf-8')
                # print(f'수신된 정보: {decodedRequest}')
                #
                # requestComponents = decodedRequest.split(',')
                #
                # receivedRequestProtocolNumber = requestComponents[0]
                # print(f"프로토콜 번호: {receivedRequestProtocolNumber}")
                #
                # cleanedElementList = []
                #
                # if len(requestComponents) > 1:
                #     for i, element in enumerate(requestComponents[1:]):
                #         byteLiteralMatch = re.search(r"b'(.+)'", element)
                #
                #         if byteLiteralMatch:
                #             byteLiteral = byteLiteralMatch.group(1)
                #             decodedElement = byteLiteral.encode('utf-8').decode('unicode_escape')
                #             cleanedElement = decodedElement.strip()
                #             print(f"후속 정보 {i + 1}: {cleanedElement}")
                #
                #             cleanedElementList.append(cleanedElement)

                response = customProtocolRepository.execute(int(protocolNumber), requestForm)
                print(f"response 응답!: {response}")

                if type(response) == AccountLoginResponse:
                    print("SocketSessionRepository: 호출 완료")
                    if response.getSessionAccountId != -1:
                        SocketSessionRepository.saveSocketSession(clientSocket, response.getSessionAccountId())

                #transmitMessage = converter.convertToTransmitMessage(protocolNumber, response)
                transmitMessage = converter.convertToData(response)
                transmitQueue.put(transmitMessage)
            except Exception as e:
                 print(f"ReceiverRepositoryImpl error: {e}")

            except socket.error as exception:
                print(f"socket error: {exception}")
                if exception.errno == errno.EWOULDBLOCK:
                    clientSocket.closeSocket()
            finally:
                sleep(0.5)