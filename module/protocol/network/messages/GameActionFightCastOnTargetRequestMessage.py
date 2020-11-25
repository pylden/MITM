from module.protocol.network.message import Message


class GameActionFightCastOnTargetRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1071
        self.spellId = {"type": "uint", "value": ""}
        self.targetId = {"type": "Number", "value": ""}
