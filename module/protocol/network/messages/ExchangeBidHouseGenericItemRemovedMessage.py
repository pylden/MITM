from module.protocol.network.message import Message


class ExchangeBidHouseGenericItemRemovedMessage(Message):
    def __init__(self):
        self.id = 8250
