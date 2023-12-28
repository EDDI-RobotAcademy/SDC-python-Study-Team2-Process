import errno
import unittest
from socket import socket
from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl
from main import initEachDomain
from request_generator.service.RequestGeneratorServiceImpl import RequestGeneratorServiceImpl
from transmitter.repository.TransmitterRepositoryImpl import TransmitterRepositoryImpl
class TestReceiveRepository(unittest.TestCase):
    def setUp(self):
        self.repository = CustomProtocolRepositoryImpl()
        self.requestGenerator = RequestGeneratorServiceImpl()
    def testReceive(self):
        # receivedForm = {
        #     "protocol": 1,
        #     "data": {
        #         "__accountId": "test_user",
        #         "__password": "password"
        #     }
        # }

        receivedForm = {
            "protocol": 1,
            "data": {
                "__accountId": "eddi",
                "__password" : "eddi@123"


            }
        }
        initEachDomain()
        transmitterRepository = TransmitterRepositoryImpl.getInstance()
        transmitQueue = transmitterRepository.getTransmitQueue()
        customProtocolRepository = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()
        try:
            protocolNumber = receivedForm["protocol"]
            receivedRequestForm = receivedForm["data"]
            print(f"typeof protocolNumber: {type(protocolNumber)}")
            print(f"protocolNumber: {protocolNumber}")
            print(f"typeof requestForm: {type(receivedRequestForm)}")
            print(f"receivedRequestForm: {receivedRequestForm}")
            requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
            print(f"requestGenerator: {requestGenerator}")
            requestForm = requestGenerator(receivedRequestForm)
            print(f"requestForm: {requestForm}")
            print(f"receiverRepository RequestForm: {requestForm.__dict__}")
            response = customProtocolRepository.execute(int(protocolNumber), tuple(requestForm.__dict__.values()))
            print(f"response: {response}")
            transmitQueue.put(response)
        except socket.error as exception:
            if exception.errno == errno.EWOULDBLOCK:
                pass