from module.protocol.network.message import Message


class GuildModificationNameVal942(Message):
    def __init__(self):
        self.id = 942
        self.guildName = {"type": "String", "value": ""}
