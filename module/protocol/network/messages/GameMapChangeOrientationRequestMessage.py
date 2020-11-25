from module.protocol.network.message import Message


class GameMapChangeOrientationRequestMessage(Message):
    def __init__(self):
        self.id = 1337
