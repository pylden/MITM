from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismSetSabotagedRefusedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1834
        self.subAreaId = {"type": "uint", "value": ""}
        self.reason = {"type": "int", "value": ""}
