from module.protocol.network.messages.NetworkMessage import NetworkMessage


class StatsUpgradeResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4819
        self.vars.append({"name": "result", "type": "int", "value": ""})
        self.vars.append({"name": "nbCharacBoost", "type": "uint", "value": ""})
