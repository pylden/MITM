from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ClientKeyMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6268
        self.key = {"type": "String", "value": ""}

    def deserialize(self):
        self.key = self.buffer_reader.read_utf()