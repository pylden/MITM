from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightActivateGlyphTrapMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4225
        self.vars.append({"name": "markId", "type": "int", "value": ""})
        self.vars.append({"name": "active", "type": "Boolean", "value": ""})
