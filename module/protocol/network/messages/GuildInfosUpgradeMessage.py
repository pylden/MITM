from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildInfosUpgradeMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2143
        self.vars.append({"name": "maxTaxCollectorsCount", "type": "uint", "value": ""})
        self.vars.append({"name": "taxCollectorsCount", "type": "uint", "value": ""})
        self.vars.append({"name": "taxCollectorLifePoints", "type": "uint", "value": ""})
        self.vars.append({"name": "taxCollectorDamagesBonuses", "type": "uint", "value": ""})
        self.vars.append({"name": "taxCollectorPods", "type": "uint", "value": ""})
        self.vars.append({"name": "taxCollectorProspecting", "type": "uint", "value": ""})
        self.vars.append({"name": "taxCollectorWisdom", "type": "uint", "value": ""})
        self.vars.append({"name": "boostPoints", "type": "uint", "value": ""})
        self.vars.append({"name": "spellId", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "spellLevel", "type": "Vector.<int>", "value": ""})
