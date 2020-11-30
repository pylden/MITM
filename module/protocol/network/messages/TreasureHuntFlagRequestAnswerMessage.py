from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntFlagRequestAnswerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8358
        self.questType = {"type": "uint", "value": ""}
        self.result = {"type": "uint", "value": ""}
        self.index = {"type": "uint", "value": ""}
