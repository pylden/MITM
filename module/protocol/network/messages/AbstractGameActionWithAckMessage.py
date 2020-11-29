from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class AbstractGameActionWithAckMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1777
        self.vars.append({"name": "waitAckId", "type": "int", "value": ""})
