from module.protocol.network.message import Message


class CharacterDeletionErrorMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6428
        self.reason = {"type": "uint", "value": ""}
