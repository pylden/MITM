from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightDodgePointLossMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9316
        self.targetId = {"type": "Number", "value": ""}
        self.amount = {"type": "uint", "value": ""}
