from module.protocol.network.message import Message


class GameFightReadyMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4679
        self.isReady = {"type": "Boolean", "value": ""}
