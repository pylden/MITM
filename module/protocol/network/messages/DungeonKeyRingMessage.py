from module.protocol.network.message import Message


class DungeonKeyRingMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6151
        self.availables = {"type": "Vector.<uint>", "value": ""}
        self.unavailables = {"type": "Vector.<uint>", "value": ""}
