from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightSpellCooldownVariationMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3484
        self.targetId = {"type": "Number", "value": ""}
        self.spellId = {"type": "uint", "value": ""}
        self.value = {"type": "int", "value": ""}
