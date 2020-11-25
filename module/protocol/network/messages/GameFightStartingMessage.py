from module.protocol.network.message import Message


class GameFightStartingMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6131
        self.fightType = {"type": "uint", "value": ""}
        self.fightId = {"type": "uint", "value": ""}
        self.attackerId = {"type": "Number", "value": ""}
        self.defenderId = {"type": "Number", "value": ""}
        self.containsBoss = {"type": "Boolean", "value": ""}
