from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildChangeMemberParametersMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2513
        self.memberId = {"type": "Number", "value": ""}
        self.rank = {"type": "uint", "value": ""}
        self.experienceGivenPercent = {"type": "uint", "value": ""}
        self.rights = {"type": "uint", "value": ""}
