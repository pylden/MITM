from module.protocol.network.message import Message


class EnabledChannelsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2771
        self.channels = {"type": "Vector.<uint>", "value": ""}
        self.disallowed = {"type": "Vector.<uint>", "value": ""}
