from module.protocol.network.message import Message


class GuildModificationNameValidMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 942
        self.guildName = {"type": "String", "value": ""}
