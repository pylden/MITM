from module.protocol.network.message import Message


class OrnamentLostMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4335
        self.ornamentId = {"type": "uint", "value": ""}
