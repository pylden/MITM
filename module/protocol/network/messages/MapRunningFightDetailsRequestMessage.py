from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MapRunningFightDetailsRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4836
        self.fightId = {"type": "uint", "value": ""}
