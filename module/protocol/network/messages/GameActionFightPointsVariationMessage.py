from module.protocol.network.message import Message


class GameActionFightPointsVariationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1965
        self.targetId = {"type": "Number", "value": ""}
        self.delta = {"type": "int", "value": ""}
