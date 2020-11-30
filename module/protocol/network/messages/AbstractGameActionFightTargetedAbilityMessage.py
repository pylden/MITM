from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class AbstractGameActionFightTargetedAbilityMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4295
        self.targetId = {"type": "Number", "value": ""}
        self.destinationCellId = {"type": "int", "value": ""}
        self.critical = {"type": "uint", "value": ""}
        self.silentCast = {"type": "Boolean", "value": ""}
        self.verboseCast = {"type": "Boolean", "value": ""}
