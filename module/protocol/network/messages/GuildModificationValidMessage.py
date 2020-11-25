from module.protocol.network.message import Message


class GuildModificationVal2304(Message):
    def __init__(self):
        self.id = 2304
        self.guildName = {"type": "String", "value": ""}
