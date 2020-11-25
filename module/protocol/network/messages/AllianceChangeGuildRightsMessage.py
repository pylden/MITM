from module.protocol.network.message import Message


class AllianceChangeGuildRightsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8726
        self.guildId = {"type": "uint", "value": ""}
        self.rights = {"type": "uint", "value": ""}
