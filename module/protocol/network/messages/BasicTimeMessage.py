from module.protocol.network.message import Message


class BasicTimeMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1002
        self.timestamp = {"type": "Number", "value": ""}
        self.timezoneOffset = {"type": "int", "value": ""}
