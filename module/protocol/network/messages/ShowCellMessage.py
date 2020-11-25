from module.protocol.network.message import Message


class ShowCellMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7767
        self.sourceId = {"type": "Number", "value": ""}
        self.cellId = {"type": "uint", "value": ""}
