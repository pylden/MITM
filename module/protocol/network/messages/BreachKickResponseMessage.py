from module.protocol.network.message import Message


class BreachKickResponseMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4542
        self.target = {"type": "CharacterMinimalInformations", "value": ""}
        self.kicked = {"type": "Boolean", "value": ""}
