from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ProtocolRequired(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5481
        self.version = {"type": "String", "value": ""}

    def deserialize(self):
        self.version["value"] = self.buffer_reader.read_utf()
