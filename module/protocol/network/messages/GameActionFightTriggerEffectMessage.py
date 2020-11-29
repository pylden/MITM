from module.protocol.network.messages.GameActionFightDispellEffectMessage import GameActionFightDispellEffectMessage


class GameActionFightTriggerEffectMessage(GameActionFightDispellEffectMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameActionFightDispellEffectMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2730
