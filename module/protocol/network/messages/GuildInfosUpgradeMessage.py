from module.protocol.network.message import Message


class GuildInfosUpgradeMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
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
