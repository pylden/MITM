from module.protocol.network.message import Message


class ObjectUseOnCharacterMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1575
        self.characterId = {"type": "Number", "value": ""}
