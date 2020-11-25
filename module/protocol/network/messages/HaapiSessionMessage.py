from module.protocol.network.message import Message


class HaapiSessionMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6833
        self.key = {"type": "String", "value": ""}
        self.type = {"type": "uint", "value": ""}
