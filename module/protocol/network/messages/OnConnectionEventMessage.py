from module.protocol.network.messages.NetworkMessage import NetworkMessage


class OnConnectionEventMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2093
        self.eventType = {"type": "uint", "value": ""}
