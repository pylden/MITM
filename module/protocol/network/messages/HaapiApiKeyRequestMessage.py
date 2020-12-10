from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HaapiApiKeyRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9286

    def serialize(self):
        pass

    def deserialize(self):
        pass
