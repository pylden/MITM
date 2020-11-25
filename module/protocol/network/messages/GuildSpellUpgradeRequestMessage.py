from module.protocol.network.message import Message


class GuildSpellUpgradeRequestMessage(Message):
    def __init__(self):
        self.id = 8084
