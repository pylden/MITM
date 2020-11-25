from module.protocol.network.message import Message


class BasicWhoIsRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7214
        self.verbose = {"type": "Boolean", "value": ""}
        self.search = {"type": "String", "value": ""}
