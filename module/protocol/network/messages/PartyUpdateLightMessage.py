from module.protocol.network.messages.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyUpdateLightMessage(AbstractPartyEventMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyEventMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8915
        self.id = {"type": "Number", "value": ""}
        self.lifePoints = {"type": "uint", "value": ""}
        self.maxLifePoints = {"type": "uint", "value": ""}
        self.prospecting = {"type": "uint", "value": ""}
        self.regenRate = {"type": "uint", "value": ""}
