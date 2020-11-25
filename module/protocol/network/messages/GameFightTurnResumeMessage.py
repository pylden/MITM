from module.protocol.network.message import Message


class GameFightTurnResumeMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1375
        self.remainingTime = {"type": "uint", "value": ""}
