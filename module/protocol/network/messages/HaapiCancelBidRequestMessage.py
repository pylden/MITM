from module.protocol.network.message import Message


class HaapiCancelBidRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9408
        self.id = {"type": "Number", "value": ""}
        self.type = {"type": "uint", "value": ""}
