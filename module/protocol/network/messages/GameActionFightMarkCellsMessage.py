from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightMarkCellsMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7743
        self.mark = {"type": "GameActionMark", "value": ""}
