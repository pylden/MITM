from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BasicPingMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9489
        self.quiet = {"type": "Boolean", "value": ""}

    def deserialize(self):
        self.quiet["value"] = self.buffer_reader.read_boolean()
