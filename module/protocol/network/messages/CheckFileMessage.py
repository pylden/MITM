from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CheckFileMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8145
        self.filenameHash = {"type": "String", "value": ""}
        self.type = {"type": "uint", "value": ""}
        self.value = {"type": "String", "value": ""}
