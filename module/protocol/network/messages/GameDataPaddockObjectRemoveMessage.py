from module.protocol.network.message import Message


class GameDataPaddockObjectRemoveMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8782
        self.cellId = {"type": "uint", "value": ""}
