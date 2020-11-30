from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BasicPongMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5053
        self.quiet = {"type": "Boolean", "value": ""}
