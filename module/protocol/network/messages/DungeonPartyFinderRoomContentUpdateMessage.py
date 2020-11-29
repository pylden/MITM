from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DungeonPartyFinderRoomContentUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6270
        self.vars.append({"name": "dungeonId", "type": "uint", "value": ""})
        self.vars.append({"name": "addedPlayers", "type": "Vector.<DungeonPartyFinderPlayer>", "value": ""})
        self.vars.append({"name": "removedPlayersIds", "type": "Vector.<Number>", "value": ""})
