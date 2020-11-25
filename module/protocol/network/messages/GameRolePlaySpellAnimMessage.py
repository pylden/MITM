from module.protocol.network.message import Message


class GameRolePlaySpellAnimMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 666
        self.casterId = {"type": "Number", "value": ""}
        self.targetCellId = {"type": "uint", "value": ""}
        self.spellId = {"type": "uint", "value": ""}
        self.spellLevel = {"type": "int", "value": ""}
