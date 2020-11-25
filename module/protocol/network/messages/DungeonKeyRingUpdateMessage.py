from module.protocol.network.message import Message


class DungeonKeyRingUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 848
        self.dungeonId = {"type": "uint", "value": ""}
        self.available = {"type": "Boolean", "value": ""}
