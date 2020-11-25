from module.protocol.network.message import Message


class ObjectUseOnCharacterMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1575
        self.characterId = {"type": "Number", "value": ""}
