from module.protocol.network.message import Message


class GameActionFightActivateGlyphTrapMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4225
        self.markId = {"type": "int", "value": ""}
        self.active = {"type": "Boolean", "value": ""}
