from transmitter.repository.TransmitterRepositoryImpl import TransmitterRepositoryImpl


class ConvertToTransmitMessage:
    __instance = None

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __init__(self):
        print("ConvertToTransmitMessage 생성자 호출")

    def convertToData(self, *arg):
        result = None
        if (type(arg[0]) == list):
            result = []
            for data in arg[0]:
                result.append(dict(data))

            # result = {"list": arr}
        else:
            try:
                result = dict(arg[0])

            except Exception as e:
                result = f"DataConverterError: {e}"
                print(e)
        print(f"data is: {result}")
        return result

    def convertToTransmitMessage(self, protocolNumber, *arg):

        transmitterRepository = TransmitterRepositoryImpl.getInstance()
        transmitQueue = transmitterRepository.getTransmitQueue()

        combinedRequestData = {
            'protocol': protocolNumber,
            'data': self.convertToData(*arg)
        }
        print(f"combinedRequestData: {combinedRequestData}")
        return combinedRequestData
        #transmitQueue.put(combinedRequestData)
