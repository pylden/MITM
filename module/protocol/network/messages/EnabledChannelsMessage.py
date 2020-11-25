from module.protocol.network.message import Message


class EnabledChannelsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2771
        self.channels = {"type": "Vector.<uint>", "value": ""}
        self.disallowed = {"type": "Vector.<uint>", "value": ""}
