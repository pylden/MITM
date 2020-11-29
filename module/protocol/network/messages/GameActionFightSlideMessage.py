from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightSlideMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9185
        self.vars.append({"name": "targetId", "type": "Number", "value": ""})
        self.vars.append({"name": "startCellId", "type": "int", "value": ""})
        self.vars.append({"name": "endCellId", "type": "int", "value": ""})
