from module.protocol.network.messages.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyNewGuestMessage(AbstractPartyEventMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyEventMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2749
        self.vars.append({"name": "guest", "type": "PartyGuestInformations", "value": ""})
