from module.protocol.network.messages.NetworkMessage import NetworkMessage


class JobCrafterDirectoryListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2113
        self.listEntries = {"type": "Vector.<JobCrafterDirectoryListEntry>", "value": ""}
