from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TrustStatusMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2030
        self.trusted = {"type": "Boolean", "value": ""}
        self.certified = {"type": "Boolean", "value": ""}
