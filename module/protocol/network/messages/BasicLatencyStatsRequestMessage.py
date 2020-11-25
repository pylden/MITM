from module.protocol.network.message import Message


class BasicLatencyStatsRequestMessage(Message):
    def __init__(self):
        self.id = 22
