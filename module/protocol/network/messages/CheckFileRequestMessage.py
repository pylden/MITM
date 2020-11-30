from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CheckFileRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4509
        self.filename = {"type": "String", "value": ""}
        self.type = {"type": "uint", "value": ""}
