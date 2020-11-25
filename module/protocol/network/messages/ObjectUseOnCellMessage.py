from module.protocol.network.message import Message


class ObjectUseOnCellMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6871
        self.cells = {"type": "uint", "value": ""}
