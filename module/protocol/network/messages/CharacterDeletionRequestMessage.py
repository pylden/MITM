from module.protocol.network.message import Message


class CharacterDeletionRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5853
        self.characterId = {"type": "Number", "value": ""}
        self.secretAnswerHash = {"type": "String", "value": ""}
