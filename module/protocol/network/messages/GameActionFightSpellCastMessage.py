from module.protocol.network.message import Message


class GameActionFightSpellCastMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3754
        self.spellId = {"type": "uint", "value": ""}
        self.spellLevel = {"type": "int", "value": ""}
        self.portalsIds = {"type": "Vector.<int>", "value": ""}
