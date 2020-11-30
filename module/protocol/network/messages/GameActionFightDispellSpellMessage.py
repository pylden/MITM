from module.protocol.network.messages.GameActionFightDispellMessage import GameActionFightDispellMessage


class GameActionFightDispellSpellMessage(GameActionFightDispellMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameActionFightDispellMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4229
        self.spellId = {"type": "uint", "value": ""}
