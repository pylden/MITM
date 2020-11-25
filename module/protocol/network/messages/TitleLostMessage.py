from module.protocol.network.message import Message


class TitleLostMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9752
        self.titleId = {"type": "uint", "value": ""}
