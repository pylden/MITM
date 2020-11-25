from module.protocol.network.message import Message


class CharacterReplayRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1391
        self.characterId = {"type": "Number", "value": ""}
