from module.protocol.network.message import Message


class GameFightStartingMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6131
        self.fightType = {"type": "uint", "value": ""}
        self.fightId = {"type": "uint", "value": ""}
        self.attackerId = {"type": "Number", "value": ""}
        self.defenderId = {"type": "Number", "value": ""}
        self.containsBoss = {"type": "Boolean", "value": ""}
