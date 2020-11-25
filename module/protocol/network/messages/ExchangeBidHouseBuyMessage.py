from module.protocol.network.message import Message


class ExchangeBidHouseBuyMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8882
        self.uid = {"type": "uint", "value": ""}
        self.qty = {"type": "uint", "value": ""}
        self.price = {"type": "Number", "value": ""}
