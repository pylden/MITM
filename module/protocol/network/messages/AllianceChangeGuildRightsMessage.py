from module.protocol.network.message import Message


class AllianceChangeGuildRightsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8726
        self.guildId = {"type": "uint", "value": ""}
        self.rights = {"type": "uint", "value": ""}
