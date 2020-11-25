from module.protocol.network.message import Message


class CharacterReplayRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1391
        self.characterId = {"type": "Number", "value": ""}
