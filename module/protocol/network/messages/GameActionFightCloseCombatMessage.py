from module.protocol.network.messages.AbstractGameActionFightTargetedAbilityMessage import AbstractGameActionFightTargetedAbilityMessage


class GameActionFightCloseCombatMessage(AbstractGameActionFightTargetedAbilityMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionFightTargetedAbilityMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1677
        self.weaponGenericId = {"type": "uint", "value": ""}
