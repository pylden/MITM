from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DungeonKeyRingUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 848
        self.dungeonId = {"type": "uint", "value": ""}
        self.available = {"type": "Boolean", "value": ""}
