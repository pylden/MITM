from module.protocol.network.message import Message


class AbstractGameActionMessage(Message):
    def __init__(self):
        self.id = 3972
