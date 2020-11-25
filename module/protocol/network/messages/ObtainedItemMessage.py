from module.protocol.network.message import Message


class ObtainedItemMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6853
        self.genericId = {"type": "uint", "value": ""}
        self.baseQuantity = {"type": "uint", "value": ""}
