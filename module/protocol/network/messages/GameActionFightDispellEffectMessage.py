from module.protocol.network.messages.GameActionFightDispellMessage import GameActionFightDispellMessage


class GameActionFightDispellEffectMessage(GameActionFightDispellMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameActionFightDispellMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 827
        self.vars.append({"name": "boostUID", "type": "uint", "value": ""})
