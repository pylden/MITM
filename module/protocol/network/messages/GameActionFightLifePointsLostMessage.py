from module.protocol.network.message import Message


class GameActionFightLifePointsLostMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2479
        self.targetId = {"type": "Number", "value": ""}
        self.loss = {"type": "uint", "value": ""}
        self.permanentDamages = {"type": "uint", "value": ""}
        self.elementId = {"type": "int", "value": ""}
