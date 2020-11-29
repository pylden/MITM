from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightTackledMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8815
        self.vars.append({"name": "tacklersIds", "type": "Vector.<Number>", "value": ""})
