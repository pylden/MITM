from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismSetSabotagedRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9154
        self.subAreaId = {"type": "uint", "value": ""}
