from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BasicWhoIsRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7214
        self.verbose = {"type": "Boolean", "value": ""}
        self.search = {"type": "String", "value": ""}
