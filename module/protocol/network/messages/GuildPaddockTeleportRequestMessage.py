from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildPaddockTeleportRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3900
        self.paddockId = {"type": "Number", "value": ""}
