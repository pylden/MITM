from module.protocol.network.message import Message


class HouseToSellListRequestMessage(Message):
    def __init__(self):
        self.id = 259
