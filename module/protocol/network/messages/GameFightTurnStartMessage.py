from module.protocol.network.message import Message


class GameFightTurnStartMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9429
        self.id = {"type": "Number", "value": ""}
        self.waitTime = {"type": "uint", "value": ""}
