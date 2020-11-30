from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightLifePointsLostMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2479
        self.targetId = {"type": "Number", "value": ""}
        self.loss = {"type": "uint", "value": ""}
        self.permanentDamages = {"type": "uint", "value": ""}
        self.elementId = {"type": "int", "value": ""}
