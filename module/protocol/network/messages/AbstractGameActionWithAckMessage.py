from module.protocol.network.message import Message


class AbstractGameActionWithAckMessage(Message):
    def __init__(self):
        self.id = 1777
