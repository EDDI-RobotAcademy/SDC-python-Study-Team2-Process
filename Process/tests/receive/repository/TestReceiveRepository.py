import errno
import unittest
from socket import socket
from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl
from main import initEachDomain
from request_generator.service.RequestGeneratorServiceImpl import RequestGeneratorServiceImpl
from tests.transmit.repository.TestTransmitRepository import TestTransmitRepository
from transmitter.repository.TransmitterRepositoryImpl import TransmitterRepositoryImpl
from utility.converter.ConvertToTransmitMessage import ConvertToTransmitMessage


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

           "protocol": 0,
           "data": {
               "__accountSessionId" : 12
           }

        }

        # receivedForm = {
        #
        #   "protocol": 10,
        #   "data": {
        #         "accountId" : -1,
        #         "productId" : 5
        #
        #
        #   }
        # }

        initEachDomain()
        transmitterRepository = TransmitterRepositoryImpl.getInstance()
        transmitQueue = transmitterRepository.getTransmitQueue()
        customProtocolRepository = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()
        converter = ConvertToTransmitMessage.getInstance()

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
            response = customProtocolRepository.execute(int(protocolNumber), requestForm)
            print(f"response 응답해라: {response}")


            #data = dict(response)
            # transmitMessage = self.sample2(protocolNumber, response)
            #transmitMessage = converter.convertToTransmitMessage(protocolNumber, response)
            transmitMessage = converter.convertToData(response)
            #transmitQueue.put(response)
           # transmitterRepository.transmitCommand()
           #  TestTransmitRepository.getInstance().callTestTransmitRepository(transmitMessage)
            transmitQueue.put(transmitMessage)

        except socket.error as exception:
            if exception.errno == errno.EWOULDBLOCK:
                pass
