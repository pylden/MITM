from module.protocol.network.message import Message


class ExchangeReplyTaxVendorMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5635
        self.objectValue = {"type": "Number", "value": ""}
        self.totalTaxValue = {"type": "Number", "value": ""}
