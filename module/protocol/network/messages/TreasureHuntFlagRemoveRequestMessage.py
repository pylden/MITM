from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntFlagRemoveRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7652
        self.questType = {"type": "uint", "value": ""}
        self.index = {"type": "uint", "value": ""}
