from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntAvailableRetryCountUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4986
        self.questType = {"type": "uint", "value": ""}
        self.availableRetryCount = {"type": "int", "value": ""}
