from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntFlagRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8451
        self.questType = {"type": "uint", "value": ""}
        self.index = {"type": "uint", "value": ""}
