from module.protocol.network.messages.PartyInvitationRequestMessage import PartyInvitationRequestMessage


class PartyInvitationArenaRequestMessage(PartyInvitationRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        PartyInvitationRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8126
