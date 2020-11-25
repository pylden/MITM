from module.protocol.network.message import Message


class HouseSellFromInsideRequestMessage(Message):
    def __init__(self):
        self.id = 8376
