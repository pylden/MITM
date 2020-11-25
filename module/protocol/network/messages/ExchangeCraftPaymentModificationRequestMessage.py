from module.protocol.network.message import Message


class ExchangeCraftPaymentModificationRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6839
        self.quantity = {"type": "Number", "value": ""}
