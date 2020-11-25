from module.protocol.network.message import Message


class StatsUpgradeResultMessage(Message):
    def __init__(self):
        self.id = 4819
