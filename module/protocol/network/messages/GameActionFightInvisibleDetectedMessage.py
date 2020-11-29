from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightInvisibleDetectedMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2560
        self.vars.append({"name": "targetId", "type": "Number", "value": ""})
        self.vars.append({"name": "cellId", "type": "int", "value": ""})
