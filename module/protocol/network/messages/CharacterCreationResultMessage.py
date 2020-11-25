from module.protocol.network.message import Message


class CharacterCreationResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7140
        self.result = {"type": "uint", "value": ""}
