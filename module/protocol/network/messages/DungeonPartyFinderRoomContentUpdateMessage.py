from module.protocol.network.message import Message


class DungeonPartyFinderRoomContentUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6270
        self.dungeonId = {"type": "uint", "value": ""}
        self.addedPlayers = {"type": "Vector.<DungeonPartyFinderPlayer>", "value": ""}
        self.removedPlayersIds = {"type": "Vector.<Number>", "value": ""}
