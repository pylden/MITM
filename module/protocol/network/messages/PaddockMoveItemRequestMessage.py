from module.protocol.network.message import Message


class PaddockMoveItemRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 815
        self.oldCellId = {"type": "uint", "value": ""}
        self.newCellId = {"type": "uint", "value": ""}
