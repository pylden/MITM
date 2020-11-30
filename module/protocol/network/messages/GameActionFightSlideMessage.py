from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightSlideMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9185
        self.targetId = {"type": "Number", "value": ""}
        self.startCellId = {"type": "int", "value": ""}
        self.endCellId = {"type": "int", "value": ""}
