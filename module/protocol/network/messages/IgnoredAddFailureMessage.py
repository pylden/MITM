from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IgnoredAddFailureMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9626
        self.reason = {"type": "uint", "value": ""}
