from module.protocol.network.message import Message


class AcquaintanceServerListMessage(Message):
    def __init__(self):
        self.id = 137
