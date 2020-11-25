from module.protocol.network.message import Message


class IgnoredAddFailureMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9626
        self.reason = {"type": "uint", "value": ""}
