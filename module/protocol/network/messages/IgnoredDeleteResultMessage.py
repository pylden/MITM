from module.protocol.network.message import Message


class IgnoredDeleteResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5614
        self.success = {"type": "Boolean", "value": ""}
        self.name = {"type": "String", "value": ""}
        self.session = {"type": "Boolean", "value": ""}
