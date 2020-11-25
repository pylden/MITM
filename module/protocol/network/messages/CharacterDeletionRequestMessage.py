from module.protocol.network.message import Message


class CharacterDeletionRequestMessage(Message):
    def __init__(self):
        self.id = 5853
        self.secretAnswerHash = {"type": "String", "value": ""}
