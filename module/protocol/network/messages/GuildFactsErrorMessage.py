from module.protocol.network.message import Message


class GuildFactsErrorMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7622
        self.guildId = {"type": "uint", "value": ""}
