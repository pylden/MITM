from module.protocol.network.message import Message


class AllianceGuildLeavingMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2611
        self.kicked = {"type": "Boolean", "value": ""}
        self.guildId = {"type": "uint", "value": ""}
