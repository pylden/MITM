from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DungeonPartyFinderAvailableDungeonsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1350
        self.dungeonIds = {"type": "Vector.<uint>", "value": ""}
