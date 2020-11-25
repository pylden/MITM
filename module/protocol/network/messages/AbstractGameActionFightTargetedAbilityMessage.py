from module.protocol.network.message import Message


class AbstractGameActionFightTargetedAbilityMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4295
        self.targetId = {"type": "Number", "value": ""}
        self.destinationCellId = {"type": "int", "value": ""}
        self.critical = {"type": "uint", "value": ""}
        self.silentCast = {"type": "Boolean", "value": ""}
        self.verboseCast = {"type": "Boolean", "value": ""}
