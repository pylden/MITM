from module.protocol.network.message import Message


class BasicPingMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9489
        self.quiet = {"type": "Boolean", "value": ""}
