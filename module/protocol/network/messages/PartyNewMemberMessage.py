from module.protocol.network.messages.PartyUpdateMessage import PartyUpdateMessage


class PartyNewMemberMessage(PartyUpdateMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        PartyUpdateMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2531
