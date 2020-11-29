from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightExchangePositionsMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 753
        self.vars.append({"name": "targetId", "type": "Number", "value": ""})
        self.vars.append({"name": "casterCellId", "type": "int", "value": ""})
        self.vars.append({"name": "targetCellId", "type": "int", "value": ""})
