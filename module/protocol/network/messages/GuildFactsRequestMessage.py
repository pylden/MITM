from module.protocol.network.message import Message


class GuildFactsRequestMessage(Message):
    def __init__(self):
        self.id = 8768
