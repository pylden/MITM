from module.protocol.network.messages.ContactLookRequestMessage import ContactLookRequestMessage


class ContactLookRequestByNameMessage(ContactLookRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ContactLookRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2201
        self.vars.append({"name": "playerName", "type": "String", "value": ""})
