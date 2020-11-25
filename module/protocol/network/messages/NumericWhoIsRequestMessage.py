from module.protocol.network.message import Message


class NumericWhoIsRequestMessage(Message):
    def __init__(self):
        self.id = 8770
