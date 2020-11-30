from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildKickRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2484
        self.kickedId = {"type": "Number", "value": ""}
