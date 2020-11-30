from module.protocol.network.messages.NetworkMessage import NetworkMessage


class JobCrafterDirectoryRemoveMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2166
        self.jobId = {"type": "uint", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
