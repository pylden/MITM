from module.protocol.network.message import Message


class HaapiCancelBidRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9408
        self.id = {"type": "Number", "value": ""}
        self.type = {"type": "uint", "value": ""}
