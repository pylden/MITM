from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildInvitationStateRecruterMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1230
        self.recrutedName = {"type": "String", "value": ""}
        self.invitationState = {"type": "uint", "value": ""}
