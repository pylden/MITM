from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightCarryCharacterMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5624
        self.targetId = {"type": "Number", "value": ""}
        self.cellId = {"type": "int", "value": ""}
