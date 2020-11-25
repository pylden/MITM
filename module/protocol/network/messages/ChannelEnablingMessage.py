from module.protocol.network.message import Message


class ChannelEnablingMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9158
        self.channel = {"type": "uint", "value": ""}
        self.enable = {"type": "Boolean", "value": ""}
