from module.protocol.network.message import Message


class GameFightStartingMessage(Message):
    def __init__(self):
        self.id = 6131
