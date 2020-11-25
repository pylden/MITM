from module.protocol.network.message import Message


class GuildMotdSetErrorMessage(Message):
    def __init__(self):
        self.id = 801
