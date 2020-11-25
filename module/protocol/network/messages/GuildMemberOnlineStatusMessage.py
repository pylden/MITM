from module.protocol.network.message import Message


class GuildMemberOnlineStatusMessage(Message):
    def __init__(self):
        self.id = 6259
