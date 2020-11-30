from module.protocol.network.messages.ContactLookRequestMessage import ContactLookRequestMessage


class ContactLookRequestByIdMessage(ContactLookRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ContactLookRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4004
        self.playerId = {"type": "Number", "value": ""}
