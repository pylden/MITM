from module.protocol.network.message import Message


class GameFightResumeMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7999
        self.spellCooldowns = {"type": "Vector.<GameFightSpellCooldown>", "value": ""}
        self.summonCount = {"type": "uint", "value": ""}
        self.bombCount = {"type": "uint", "value": ""}
