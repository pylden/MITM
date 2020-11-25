from module.protocol.network.message import Message


class GuildMemberSetWarnOnConnectionMessage(Message):
    def __init__(self):
        self.id = 9973
