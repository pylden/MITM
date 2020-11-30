from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceInvitationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7156
        self.targetId = {"type": "Number", "value": ""}
