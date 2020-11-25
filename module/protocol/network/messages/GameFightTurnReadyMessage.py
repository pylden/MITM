from module.protocol.network.message import Message


class GameFightTurnReadyMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 983
        self.isReady = {"type": "Boolean", "value": ""}
