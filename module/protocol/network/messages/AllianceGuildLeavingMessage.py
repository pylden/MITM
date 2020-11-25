from module.protocol.network.message import Message


class AllianceGuildLeavingMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2611
        self.kicked = {"type": "Boolean", "value": ""}
        self.guildId = {"type": "uint", "value": ""}
