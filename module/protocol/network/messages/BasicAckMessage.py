from module.protocol.network.message import Message


class BasicAckMessage(Message):
    def __init__(self):
        self.id = 4378
