from module.protocol.network.message import Message


class CharacterNameSuggestionSuccessMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 421
        self.suggestion = {"type": "String", "value": ""}
