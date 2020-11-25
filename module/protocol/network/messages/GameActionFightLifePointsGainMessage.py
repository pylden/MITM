from module.protocol.network.message import Message


class GameActionFightLifePointsGainMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5687
        self.targetId = {"type": "Number", "value": ""}
        self.delta = {"type": "uint", "value": ""}
