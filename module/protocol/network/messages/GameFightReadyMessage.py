from module.protocol.network.message import Message


class GameFightReadyMessage(Message):
    def __init__(self):
        self.id = 4679
