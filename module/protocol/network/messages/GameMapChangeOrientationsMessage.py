from module.protocol.network.message import Message


class GameMapChangeOrientationsMessage(Message):
    def __init__(self):
        self.id = 1921
