from module.protocol.network.message import Message


class PaddockToSellListRequestMessage(Message):
    def __init__(self):
        self.id = 3095
