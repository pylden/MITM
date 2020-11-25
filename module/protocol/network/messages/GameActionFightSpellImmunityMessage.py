from module.protocol.network.message import Message


class GameActionFightSpellImmunityMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6537
        self.targetId = {"type": "Number", "value": ""}
        self.spellId = {"type": "uint", "value": ""}
