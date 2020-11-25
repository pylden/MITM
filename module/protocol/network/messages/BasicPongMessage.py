from module.protocol.network.message import Message


class BasicPongMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5053
        self.quiet = {"type": "Boolean", "value": ""}
