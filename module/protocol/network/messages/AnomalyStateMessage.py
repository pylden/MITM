from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AnomalyStateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4556
        self.subAreaId = {"type": "uint", "value": ""}
        self.open = {"type": "Boolean", "value": ""}
        self.closingTime = {"type": "Number", "value": ""}
