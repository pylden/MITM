from module.protocol.network.message import Message


class GameActionFightModifyEffectsDurationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6919
        self.targetId = {"type": "Number", "value": ""}
        self.delta = {"type": "int", "value": ""}
