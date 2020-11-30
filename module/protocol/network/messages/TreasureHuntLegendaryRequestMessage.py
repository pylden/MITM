from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntLegendaryRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5580
        self.legendaryId = {"type": "uint", "value": ""}
