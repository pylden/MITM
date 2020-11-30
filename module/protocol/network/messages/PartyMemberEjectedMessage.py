from module.protocol.network.messages.PartyMemberRemoveMessage import PartyMemberRemoveMessage


class PartyMemberEjectedMessage(PartyMemberRemoveMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        PartyMemberRemoveMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7534
        self.kickerId = {"type": "Number", "value": ""}
