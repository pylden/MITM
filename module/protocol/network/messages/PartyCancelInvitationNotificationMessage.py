from module.protocol.network.messages.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyCancelInvitationNotificationMessage(AbstractPartyEventMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyEventMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1253
        self.vars.append({"name": "cancelerId", "type": "Number", "value": ""})
        self.vars.append({"name": "guestId", "type": "Number", "value": ""})
