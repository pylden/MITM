from module.protocol.network.message import Message


class GameFightHumanReadyStateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 386
        self.characterId = {"type": "Number", "value": ""}
        self.isReady = {"type": "Boolean", "value": ""}
