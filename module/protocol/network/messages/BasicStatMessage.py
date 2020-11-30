from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BasicStatMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9271
        self.timeSpent = {"type": "Number", "value": ""}
        self.statId = {"type": "uint", "value": ""}
