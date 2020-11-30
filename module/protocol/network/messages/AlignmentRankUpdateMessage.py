from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AlignmentRankUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4604
        self.alignmentRank = {"type": "uint", "value": ""}
        self.verbose = {"type": "Boolean", "value": ""}
