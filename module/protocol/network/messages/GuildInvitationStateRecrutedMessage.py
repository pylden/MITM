from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildInvitationStateRecrutedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4418
        self.vars.append({"name": "invitationState", "type": "uint", "value": ""})
