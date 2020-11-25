from module.protocol.network.message import Message


class CharacterCreationResultMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7140
        self.result = {"type": "uint", "value": ""}
