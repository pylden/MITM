from module.protocol.network.message import Message


class GameFightHumanReadyStateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 386
        self.characterId = {"type": "Number", "value": ""}
        self.isReady = {"type": "Boolean", "value": ""}
