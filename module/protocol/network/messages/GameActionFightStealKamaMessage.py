from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightStealKamaMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7772
        self.targetId = {"type": "Number", "value": ""}
        self.amount = {"type": "Number", "value": ""}
