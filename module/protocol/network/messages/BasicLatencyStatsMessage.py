from module.protocol.network.message import Message


class BasicLatencyStatsMessage(Message):
    def __init__(self):
        self.id = 6675
