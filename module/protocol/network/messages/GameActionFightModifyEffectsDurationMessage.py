from module.protocol.network.message import Message


class GameActionFightModifyEffectsDurationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6919
        self.targetId = {"type": "Number", "value": ""}
        self.delta = {"type": "int", "value": ""}
