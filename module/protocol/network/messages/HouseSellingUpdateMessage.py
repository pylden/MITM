from module.protocol.network.message import Message


class HouseSellingUpdateMessage(Message):
    def __init__(self):
        self.id = 5119
        self.buyerName = {"type": "String", "value": ""}
