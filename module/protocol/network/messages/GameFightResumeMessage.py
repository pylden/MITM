from module.protocol.network.message import Message


class GameFightResumeMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7999
        self.spellCooldowns = {"type": "Vector.<GameFightSpellCooldown>", "value": ""}
        self.summonCount = {"type": "uint", "value": ""}
        self.bombCount = {"type": "uint", "value": ""}
