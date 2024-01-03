class SocketSessionRepository:
    __socketSession = {}

    @staticmethod
    def saveSocketSession(socket, sessionId):
        SocketSessionRepository.__socketSession[socket] = sessionId
        print("SocketSessionRepository: 저장 완료")

    @staticmethod
    def getSocketSession():
        return SocketSessionRepository.__socketSession

    @staticmethod
    def deleteSocketSession(socket):
        del SocketSessionRepository.__socketSession[socket]
        print("SocketSessionRepository: 삭제 완료")