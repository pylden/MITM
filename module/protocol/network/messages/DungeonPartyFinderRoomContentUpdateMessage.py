from module.protocol.network.message import Message


class DungeonPartyFinderRoomContentUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6270
        self.dungeonId = {"type": "uint", "value": ""}
        self.addedPlayers = {"type": "Vector.<DungeonPartyFinderPlayer>", "value": ""}
        self.removedPlayersIds = {"type": "Vector.<Number>", "value": ""}
