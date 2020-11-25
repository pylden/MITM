from module.protocol.network.message import Message


class GameActionFightCastOnTargetRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1071
        self.spellId = {"type": "uint", "value": ""}
        self.targetId = {"type": "Number", "value": ""}
