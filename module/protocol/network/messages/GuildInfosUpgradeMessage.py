from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildInfosUpgradeMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2143
        self.maxTaxCollectorsCount = {"type": "uint", "value": ""}
        self.taxCollectorsCount = {"type": "uint", "value": ""}
        self.taxCollectorLifePoints = {"type": "uint", "value": ""}
        self.taxCollectorDamagesBonuses = {"type": "uint", "value": ""}
        self.taxCollectorPods = {"type": "uint", "value": ""}
        self.taxCollectorProspecting = {"type": "uint", "value": ""}
        self.taxCollectorWisdom = {"type": "uint", "value": ""}
        self.boostPoints = {"type": "uint", "value": ""}
        self.spellId = {"type": "Vector.<uint>", "value": ""}
        self.spellLevel = {"type": "Vector.<int>", "value": ""}
