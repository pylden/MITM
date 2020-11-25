from module.protocol.network.message import Message


class GameActionFightLifePointsLostMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2479
        self.targetId = {"type": "Number", "value": ""}
        self.loss = {"type": "uint", "value": ""}
        self.permanentDamages = {"type": "uint", "value": ""}
        self.elementId = {"type": "int", "value": ""}
