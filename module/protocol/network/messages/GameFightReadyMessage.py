from module.protocol.network.message import Message


class GameFightReadyMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4679
        self.isReady = {"type": "Boolean", "value": ""}
