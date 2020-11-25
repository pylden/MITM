from module.protocol.network.message import Message


class GuildModificationNameVal942(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 942
        self.guildName = {"type": "String", "value": ""}
