from module.protocol.network.message import Message


class GuildMemberLeavingMessage(Message):
    def __init__(self):
        self.id = 2202
