from module.protocol.network.message import Message


class GameActionFightCastRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8507
        self.spellId = {"type": "uint", "value": ""}
        self.cellId = {"type": "int", "value": ""}
