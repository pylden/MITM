from module.protocol.network.message import Message


class GameFightTurnReadyMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 983
        self.isReady = {"type": "Boolean", "value": ""}
