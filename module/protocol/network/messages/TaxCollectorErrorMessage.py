from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TaxCollectorErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3339
        self.reason = {"type": "int", "value": ""}
