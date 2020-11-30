from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildInformationsMembersMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1702
        self.members = {"type": "Vector.<GuildMember>", "value": ""}
