from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DungeonPartyFinderRoomContentMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8587
        self.dungeonId = {"type": "uint", "value": ""}
        self.players = {"type": "Vector.<DungeonPartyFinderPlayer>", "value": ""}
