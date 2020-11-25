from module.protocol.network.message import Message


class PaddockBuyRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6999
        self.proposedPrice = {"type": "Number", "value": ""}
