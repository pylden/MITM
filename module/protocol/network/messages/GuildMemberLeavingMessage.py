from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildMemberLeavingMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2202
        self.kicked = {"type": "Boolean", "value": ""}
        self.memberId = {"type": "Number", "value": ""}
