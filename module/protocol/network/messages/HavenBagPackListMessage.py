from module.protocol.network.message import Message


class HavenBagPackListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6073
        self.packIds = {"type": "Vector.<int>", "value": ""}
