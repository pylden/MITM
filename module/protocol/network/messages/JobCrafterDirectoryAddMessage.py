from module.protocol.network.messages.NetworkMessage import NetworkMessage


class JobCrafterDirectoryAddMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2605
        self.listEntry = {"type": "JobCrafterDirectoryListEntry", "value": ""}
