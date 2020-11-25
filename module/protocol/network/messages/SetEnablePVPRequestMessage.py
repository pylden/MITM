from module.protocol.network.message import Message


class SetEnablePVPRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4606
        self.enable = {"type": "Boolean", "value": ""}
