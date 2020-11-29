from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightSpellCooldownVariationMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3484
        self.vars.append({"name": "targetId", "type": "Number", "value": ""})
        self.vars.append({"name": "spellId", "type": "uint", "value": ""})
        self.vars.append({"name": "value", "type": "int", "value": ""})
