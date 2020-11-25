from module.protocol.network.message import Message


class ClientUIOpenedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1056
        self.type = {"type": "uint", "value": ""}
