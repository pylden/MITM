from module.protocol.network.message import Message


class GuildSpellUpgradeRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8084
        self.spellId = {"type": "uint", "value": ""}
