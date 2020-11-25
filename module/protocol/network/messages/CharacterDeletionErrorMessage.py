from module.protocol.network.message import Message


class CharacterDeletionErrorMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6428
        self.reason = {"type": "uint", "value": ""}
