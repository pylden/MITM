from module.protocol.network.message import Message


class GuildMotdSetRequestMessage(Message):
    def __init__(self):
        self.id = 2776
        self.content = {"type": "String", "value": ""}
