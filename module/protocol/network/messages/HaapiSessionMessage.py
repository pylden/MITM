from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HaapiSessionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6833
        self.key = {"type": "String", "value": ""}
        self.type = {"type": "uint", "value": ""}
