from module.protocol.network.message import Message


class TitleSelectRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7473
        self.titleId = {"type": "uint", "value": ""}
