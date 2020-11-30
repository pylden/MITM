from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ZaapRespawnUpdatedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3597
        self.mapId = {"type": "Number", "value": ""}
