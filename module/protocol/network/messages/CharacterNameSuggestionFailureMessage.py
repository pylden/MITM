from module.protocol.network.message import Message


class CharacterNameSuggestionFailureMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 768
        self.reason = {"type": "uint", "value": ""}
