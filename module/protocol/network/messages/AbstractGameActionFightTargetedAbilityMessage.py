from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class AbstractGameActionFightTargetedAbilityMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4295
        self.vars.append({"name": "targetId", "type": "Number", "value": ""})
        self.vars.append({"name": "destinationCellId", "type": "int", "value": ""})
        self.vars.append({"name": "critical", "type": "uint", "value": ""})
        self.vars.append({"name": "silentCast", "type": "Boolean", "value": ""})
        self.vars.append({"name": "verboseCast", "type": "Boolean", "value": ""})
