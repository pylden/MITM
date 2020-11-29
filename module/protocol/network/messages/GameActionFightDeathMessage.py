from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightDeathMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4815
        self.vars.append({"name": "targetId", "type": "Number", "value": ""})
