from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceInvitationStateRecrutedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5125
        self.vars.append({"name": "invitationState", "type": "uint", "value": ""})
