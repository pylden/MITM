from module.protocol.network.message import Message


class BreachSavedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8940
        self.saved = {"type": "Boolean", "value": ""}
