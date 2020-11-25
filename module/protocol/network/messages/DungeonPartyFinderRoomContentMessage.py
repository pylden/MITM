from module.protocol.network.message import Message


class DungeonPartyFinderRoomContentMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8587
        self.dungeonId = {"type": "uint", "value": ""}
        self.players = {"type": "Vector.<DungeonPartyFinderPlayer>", "value": ""}
