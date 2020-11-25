from module.protocol.network.message import Message


class GameActionFightSpellCooldownVariationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3484
        self.targetId = {"type": "Number", "value": ""}
        self.spellId = {"type": "uint", "value": ""}
        self.value = {"type": "int", "value": ""}
