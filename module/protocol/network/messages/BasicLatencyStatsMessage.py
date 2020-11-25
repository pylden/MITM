from module.protocol.network.message import Message


class BasicLatencyStatsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6675
        self.latency = {"type": "uint", "value": ""}
        self.sampleCount = {"type": "uint", "value": ""}
        self.max = {"type": "uint", "value": ""}
