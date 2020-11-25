from module.protocol.network.message import Message


class ExchangeBidHouseBuyMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8882
        self.uid = {"type": "uint", "value": ""}
        self.qty = {"type": "uint", "value": ""}
        self.price = {"type": "Number", "value": ""}
