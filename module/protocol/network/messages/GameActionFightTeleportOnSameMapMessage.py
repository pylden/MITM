from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightTeleportOnSameMapMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2698
        self.targetId = {"type": "Number", "value": ""}
        self.cellId = {"type": "int", "value": ""}
