from module.protocol.network.message import Message


class BasicLatencyStatsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6675
        self.latency = {"type": "uint", "value": ""}
        self.sampleCount = {"type": "uint", "value": ""}
        self.max = {"type": "uint", "value": ""}
