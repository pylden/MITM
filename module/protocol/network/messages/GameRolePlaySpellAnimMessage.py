from module.protocol.network.message import Message


class GameRolePlaySpellAnimMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 666
        self.casterId = {"type": "Number", "value": ""}
        self.targetCellId = {"type": "uint", "value": ""}
        self.spellId = {"type": "uint", "value": ""}
        self.spellLevel = {"type": "int", "value": ""}
