from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HaapiTokenMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9546
        self.token = {"type": "String", "value": ""}
