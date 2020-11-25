from module.protocol.network.message import Message


class IgnoredAddRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9784
        self.name = {"type": "String", "value": ""}
        self.session = {"type": "Boolean", "value": ""}
