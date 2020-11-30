from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightTriggerGlyphTrapMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9588
        self.markId = {"type": "int", "value": ""}
        self.markImpactCell = {"type": "uint", "value": ""}
        self.triggeringCharacterId = {"type": "Number", "value": ""}
        self.triggeredSpellId = {"type": "uint", "value": ""}
