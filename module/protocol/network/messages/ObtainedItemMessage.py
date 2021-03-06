from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ObtainedItemMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6853
        self.genericId = {"type": "uint", "value": ""}
        self.baseQuantity = {"type": "uint", "value": ""}
