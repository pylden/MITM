from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightReduceDamagesMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3507
        self.vars.append({"name": "targetId", "type": "Number", "value": ""})
        self.vars.append({"name": "amount", "type": "uint", "value": ""})
