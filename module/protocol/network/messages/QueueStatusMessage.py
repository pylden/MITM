from module.protocol.network.messages.NetworkMessage import NetworkMessage


class QueueStatusMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9955
        self.position = {"type": "uint", "value": ""}
        self.total = {"type": "uint", "value": ""}
