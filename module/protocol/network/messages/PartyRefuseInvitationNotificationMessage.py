from module.protocol.network.messages.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyRefuseInvitationNotificationMessage(AbstractPartyEventMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyEventMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9862
        self.guestId = {"type": "Number", "value": ""}
