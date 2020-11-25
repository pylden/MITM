from module.protocol.network.message import Message


class GameActionFightLifePointsGainMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5687
        self.targetId = {"type": "Number", "value": ""}
        self.delta = {"type": "uint", "value": ""}
