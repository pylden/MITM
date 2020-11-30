from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ObjectJobAddedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 355
        self.jobId = {"type": "uint", "value": ""}
