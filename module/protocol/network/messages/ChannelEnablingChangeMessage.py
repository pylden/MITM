from module.protocol.network.message import Message


class ChannelEnablingChangeMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3541
        self.channel = {"type": "uint", "value": ""}
        self.enable = {"type": "Boolean", "value": ""}
