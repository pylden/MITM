from module.protocol.network.message import Message


class GuildSpellUpgradeRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8084
        self.spellId = {"type": "uint", "value": ""}
