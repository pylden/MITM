from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BasicLatencyStatsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6675
        self.vars.append({"name": "latency", "type": "uint", "value": ""})
        self.vars.append({"name": "sampleCount", "type": "uint", "value": ""})
        self.vars.append({"name": "max", "type": "uint", "value": ""})
