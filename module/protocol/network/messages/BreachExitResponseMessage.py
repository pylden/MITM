from module.protocol.network.message import Message


class BreachExitResponseMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 624
        self.exited = {"type": "Boolean", "value": ""}
