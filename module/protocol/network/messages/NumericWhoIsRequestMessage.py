from module.protocol.network.messages.NetworkMessage import NetworkMessage


class NumericWhoIsRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8770
        self.playerId = {"type": "Number", "value": ""}
