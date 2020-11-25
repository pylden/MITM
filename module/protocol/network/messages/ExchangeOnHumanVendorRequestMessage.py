from module.protocol.network.message import Message


class ExchangeOnHumanVendorRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9270
        self.humanVendorId = {"type": "Number", "value": ""}
        self.humanVendorCell = {"type": "uint", "value": ""}
