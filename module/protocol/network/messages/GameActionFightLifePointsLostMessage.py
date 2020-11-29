from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightLifePointsLostMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2479
        self.vars.append({"name": "targetId", "type": "Number", "value": ""})
        self.vars.append({"name": "loss", "type": "uint", "value": ""})
        self.vars.append({"name": "permanentDamages", "type": "uint", "value": ""})
        self.vars.append({"name": "elementId", "type": "int", "value": ""})
