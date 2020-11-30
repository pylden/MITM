from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightUnmarkCellsMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3826
        self.markId = {"type": "int", "value": ""}
