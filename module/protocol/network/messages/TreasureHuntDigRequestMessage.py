from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntDigRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6086
        self.questType = {"type": "uint", "value": ""}
