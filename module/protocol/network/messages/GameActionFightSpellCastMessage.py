from module.protocol.network.message import Message


class GameActionFightSpellCastMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3754
        self.spellId = {"type": "uint", "value": ""}
        self.spellLevel = {"type": "int", "value": ""}
        self.portalsIds = {"type": "Vector.<int>", "value": ""}
