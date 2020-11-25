from module.protocol.network.message import Message


class GameActionFightSpellImmunityMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6537
        self.targetId = {"type": "Number", "value": ""}
        self.spellId = {"type": "uint", "value": ""}
