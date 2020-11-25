from module.protocol.network.message import Message


class ExchangeReplyTaxVendorMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5635
        self.objectValue = {"type": "Number", "value": ""}
        self.totalTaxValue = {"type": "Number", "value": ""}
