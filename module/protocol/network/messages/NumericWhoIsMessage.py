from module.protocol.network.message import Message


class NumericWhoIsMessage(Message):
    def __init__(self):
        self.id = 9545
