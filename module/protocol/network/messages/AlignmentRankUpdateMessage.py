from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AlignmentRankUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4604
        self.vars.append({"name": "alignmentRank", "type": "uint", "value": ""})
        self.vars.append({"name": "verbose", "type": "Boolean", "value": ""})
