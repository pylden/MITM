from module.protocol.network.message import Message


class GuildFightJoinRequestMessage(Message):
    def __init__(self):
        self.id = 6522
