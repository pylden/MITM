from module.protocol.network.messages.NetworkMessage import NetworkMessage


class StatsUpgradeRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2014
        self.useAdditionnal = {"type": "Boolean", "value": ""}
        self.statId = {"type": "uint", "value": ""}
        self.boostPoint = {"type": "uint", "value": ""}
