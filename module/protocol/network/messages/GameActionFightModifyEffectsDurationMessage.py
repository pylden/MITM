from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightModifyEffectsDurationMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6919
        self.targetId = {"type": "Number", "value": ""}
        self.delta = {"type": "int", "value": ""}
