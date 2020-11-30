from module.protocol.network.messages.AbstractGameActionFightTargetedAbilityMessage import AbstractGameActionFightTargetedAbilityMessage


class GameActionFightSpellCastMessage(AbstractGameActionFightTargetedAbilityMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionFightTargetedAbilityMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3754
        self.spellId = {"type": "uint", "value": ""}
        self.spellLevel = {"type": "int", "value": ""}
        self.portalsIds = {"type": "Vector.<int>", "value": ""}
