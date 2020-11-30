from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightDispellMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7134
        self.targetId = {"type": "Number", "value": ""}
        self.verboseCast = {"type": "Boolean", "value": ""}
