from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightDispellMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7134
        self.vars.append({"name": "targetId", "type": "Number", "value": ""})
        self.vars.append({"name": "verboseCast", "type": "Boolean", "value": ""})
