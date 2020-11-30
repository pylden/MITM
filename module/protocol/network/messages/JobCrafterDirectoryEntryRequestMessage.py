from module.protocol.network.messages.NetworkMessage import NetworkMessage


class JobCrafterDirectoryEntryRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2083
        self.playerId = {"type": "Number", "value": ""}
