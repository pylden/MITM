from module.protocol.network.message import Message


class CharacterNameSuggestionFailureMessage(Message):
    def __init__(self):
        self.id = 768
