from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceInvitationAnswerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6986
        self.accept = {"type": "Boolean", "value": ""}
