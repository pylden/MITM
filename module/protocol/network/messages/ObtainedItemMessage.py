from module.protocol.network.message import Message


class ObtainedItemMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6853
        self.genericId = {"type": "uint", "value": ""}
        self.baseQuantity = {"type": "uint", "value": ""}
