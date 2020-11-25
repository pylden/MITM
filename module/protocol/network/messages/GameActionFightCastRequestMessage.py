from module.protocol.network.message import Message


class GameActionFightCastRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8507
        self.spellId = {"type": "uint", "value": ""}
        self.cellId = {"type": "int", "value": ""}
