from module.protocol.network.message import Message


class SetEnableAVARequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4687
        self.enable = {"type": "Boolean", "value": ""}
