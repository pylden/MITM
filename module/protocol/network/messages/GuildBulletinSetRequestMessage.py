from module.protocol.network.message import Message


class GuildBulletinSetRequestMessage(Message):
    def __init__(self):
        self.id = 2821
        self.content = {"type": "String", "value": ""}
