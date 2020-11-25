from module.protocol.network.message import Message


class PaddockBuyRequestMessage(Message):
    def __init__(self):
        self.id = 6999
