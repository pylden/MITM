from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightTriggerGlyphTrapMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9588
        self.vars.append({"name": "markId", "type": "int", "value": ""})
        self.vars.append({"name": "markImpactCell", "type": "uint", "value": ""})
        self.vars.append({"name": "triggeringCharacterId", "type": "Number", "value": ""})
        self.vars.append({"name": "triggeredSpellId", "type": "uint", "value": ""})
