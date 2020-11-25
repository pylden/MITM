from module.protocol.network.message import Message


class ExchangeOnHumanVendorRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9270
        self.humanVendorId = {"type": "Number", "value": ""}
        self.humanVendorCell = {"type": "uint", "value": ""}
