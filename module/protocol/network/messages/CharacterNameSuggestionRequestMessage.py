from module.protocol.network.message import Message


class CharacterNameSuggestionRequestMessage(Message):
    def __init__(self):
        self.id = 5249
