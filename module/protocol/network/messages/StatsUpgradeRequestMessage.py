from module.protocol.network.message import Message


class StatsUpgradeRequestMessage(Message):
    def __init__(self):
        self.id = 2014
