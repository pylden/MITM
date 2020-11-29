from module.protocol.network.messages.PartyInvitationRequestMessage import PartyInvitationRequestMessage


class PartyInvitationDungeonRequestMessage(PartyInvitationRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        PartyInvitationRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3567
        self.vars.append({"name": "dungeonId", "type": "uint", "value": ""})
