from module.protocol.network.messages.NetworkMessage import NetworkMessage


class OrnamentSelectErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9564
        self.reason = {"type": "uint", "value": ""}
