from module.protocol.network.message import Message


class PaddockToSellFilterMessage(Message):
    def __init__(self):
        self.id = 1083
