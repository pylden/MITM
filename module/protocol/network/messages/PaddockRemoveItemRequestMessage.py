from module.protocol.network.message import Message


class PaddockRemoveItemRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6943
        self.cellId = {"type": "uint", "value": ""}
