from module.protocol.network.message import Message


class CharacterSelectedForceMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6332
        self.id = {"type": "int", "value": ""}
