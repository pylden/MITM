from module.protocol.network.messages.NetworkMessage import NetworkMessage


class RecycleResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3014
        self.nuggetsForPrism = {"type": "uint", "value": ""}
        self.nuggetsForPlayer = {"type": "uint", "value": ""}
