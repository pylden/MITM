from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IgnoredDeleteRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7856
        self.accountId = {"type": "uint", "value": ""}
        self.session = {"type": "Boolean", "value": ""}
