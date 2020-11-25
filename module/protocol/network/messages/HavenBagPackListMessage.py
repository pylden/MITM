from module.protocol.network.message import Message


class HavenBagPackListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6073
        self.packIds = {"type": "Vector.<int>", "value": ""}
