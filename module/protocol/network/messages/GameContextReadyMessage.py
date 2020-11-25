from module.protocol.network.message import Message


class GameContextReadyMessage(Message):
    def __init__(self):
        self.id = 6225
