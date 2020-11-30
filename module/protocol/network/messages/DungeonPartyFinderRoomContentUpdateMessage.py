from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DungeonPartyFinderRoomContentUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6270
        self.dungeonId = {"type": "uint", "value": ""}
        self.addedPlayers = {"type": "Vector.<DungeonPartyFinderPlayer>", "value": ""}
        self.removedPlayersIds = {"type": "Vector.<Number>", "value": ""}
