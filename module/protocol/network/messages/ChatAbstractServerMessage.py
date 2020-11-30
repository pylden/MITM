from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChatAbstractServerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1532
        self.channel = {"type": "uint", "value": ""}
        self.content = {"type": "String", "value": ""}
        self.timestamp = {"type": "uint", "value": ""}
        self.fingerprint = {"type": "String", "value": ""}
