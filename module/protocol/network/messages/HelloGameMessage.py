from module.protocol.network.message import Message


class HelloGameMessage(Message):
    def __init__(self):
        self.id = 8008