from module.protocol.network.message import Message


class ExchangeBuyMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4224
        self.objectToBuyId = {"type": "uint", "value": ""}
        self.quantity = {"type": "uint", "value": ""}
