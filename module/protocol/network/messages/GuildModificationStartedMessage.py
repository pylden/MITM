from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildModificationStartedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2536
        self.canChangeName = {"type": "Boolean", "value": ""}
        self.canChangeEmblem = {"type": "Boolean", "value": ""}
