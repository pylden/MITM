from module.protocol.network.message import Message


class GameFightTurnStartMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9429
        self.id = {"type": "Number", "value": ""}
        self.waitTime = {"type": "uint", "value": ""}
