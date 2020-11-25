from module.protocol.network.message import Message


class GameActionFightActivateGlyphTrapMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4225
        self.markId = {"type": "int", "value": ""}
        self.active = {"type": "Boolean", "value": ""}
