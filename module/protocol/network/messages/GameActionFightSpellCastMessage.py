from module.protocol.network.messages.AbstractGameActionFightTargetedAbilityMessage import AbstractGameActionFightTargetedAbilityMessage


class GameActionFightSpellCastMessage(AbstractGameActionFightTargetedAbilityMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionFightTargetedAbilityMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3754
        self.vars.append({"name": "spellId", "type": "uint", "value": ""})
        self.vars.append({"name": "spellLevel", "type": "int", "value": ""})
        self.vars.append({"name": "portalsIds", "type": "Vector.<int>", "value": ""})
