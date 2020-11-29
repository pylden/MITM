from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightChangeLookMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3680
        self.vars.append({"name": "targetId", "type": "Number", "value": ""})
        self.vars.append({"name": "entityLook", "type": "EntityLook", "value": ""})
