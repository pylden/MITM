from module.protocol.network.message import Message


class GameFightTurnResumeMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1375
        self.remainingTime = {"type": "uint", "value": ""}
