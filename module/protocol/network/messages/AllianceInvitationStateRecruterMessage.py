from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceInvitationStateRecruterMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4543
        self.recrutedName = {"type": "String", "value": ""}
        self.invitationState = {"type": "uint", "value": ""}
