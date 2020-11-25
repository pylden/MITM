from module.protocol.network.message import Message


class GuildMemberWarnOnConnectionStateMessage(Message):
    def __init__(self):
        self.id = 3164
