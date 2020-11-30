from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BasicLatencyStatsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6675
        self.latency = {"type": "uint", "value": ""}
        self.sampleCount = {"type": "uint", "value": ""}
        self.max = {"type": "uint", "value": ""}
