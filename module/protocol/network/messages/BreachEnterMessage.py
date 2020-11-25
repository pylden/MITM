from module.protocol.network.message import Message


class BreachEnterMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3176
        self.owner = {"type": "Number", "value": ""}
