from module.protocol.network.messages.NetworkMessage import NetworkMessage


class JobCrafterDirectoryAddMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2605
        self.vars.append({"name": "listEntry", "type": "JobCrafterDirectoryListEntry", "value": ""})
