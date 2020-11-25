from module.protocol.network.message import Message


class OrnamentSelectedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7227
        self.ornamentId = {"type": "uint", "value": ""}
