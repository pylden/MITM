from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightExchangePositionsMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 753
        self.targetId = {"type": "Number", "value": ""}
        self.casterCellId = {"type": "int", "value": ""}
        self.targetCellId = {"type": "int", "value": ""}
