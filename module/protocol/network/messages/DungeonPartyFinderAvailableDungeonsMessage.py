from module.protocol.network.message import Message


class DungeonPartyFinderAvailableDungeonsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1350
        self.dungeonIds = {"type": "Vector.<uint>", "value": ""}
