from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TaxCollectorAttackedResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8211
        self.vars.append({"name": "deadOrAlive", "type": "Boolean", "value": ""})
        self.vars.append({"name": "basicInfos", "type": "TaxCollectorBasicInformations", "value": ""})
        self.vars.append({"name": "guild", "type": "BasicGuildInformations", "value": ""})
