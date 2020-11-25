from module.protocol.network.message import Message


class ChatErrorMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5057
        self.reason = {"type": "uint", "value": ""}
