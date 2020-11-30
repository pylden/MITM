from module.protocol.network.messages.NetworkMessage import NetworkMessage


class OrnamentLostMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4335
        self.ornamentId = {"type": "uint", "value": ""}
