from module.protocol.network.messages.NetworkMessage import NetworkMessage


class StatsUpgradeRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2014
        self.vars.append({"name": "useAdditionnal", "type": "Boolean", "value": ""})
        self.vars.append({"name": "statId", "type": "uint", "value": ""})
        self.vars.append({"name": "boostPoint", "type": "uint", "value": ""})
