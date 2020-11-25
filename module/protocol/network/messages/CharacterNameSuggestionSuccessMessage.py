from module.protocol.network.message import Message


class CharacterNameSuggestionSuccessMessage(Message):
    def __init__(self):
        self.id = 421
        self.suggestion = {"type": "String", "value": ""}
