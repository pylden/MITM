from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildFightJoinRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6522
        self.taxCollectorId = {"type": "Number", "value": ""}
