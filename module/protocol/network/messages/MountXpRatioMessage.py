from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MountXpRatioMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9818
        self.ratio = {"type": "uint", "value": ""}
