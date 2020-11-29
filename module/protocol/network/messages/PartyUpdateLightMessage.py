from module.protocol.network.messages.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyUpdateLightMessage(AbstractPartyEventMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyEventMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8915
        self.vars.append({"name": "id", "type": "Number", "value": ""})
        self.vars.append({"name": "lifePoints", "type": "uint", "value": ""})
        self.vars.append({"name": "maxLifePoints", "type": "uint", "value": ""})
        self.vars.append({"name": "prospecting", "type": "uint", "value": ""})
        self.vars.append({"name": "regenRate", "type": "uint", "value": ""})
