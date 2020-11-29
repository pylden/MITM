from module.protocol.network.messages.AbstractPartyMessage import AbstractPartyMessage


class PartyRefuseInvitationMessage(AbstractPartyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1909
