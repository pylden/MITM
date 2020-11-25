from module.protocol.network.message import Message


class DungeonPartyFinderAvailableDungeonsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1350
        self.dungeonIds = {"type": "Vector.<uint>", "value": ""}
