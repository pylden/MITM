from module.protocol.network.messages.PartyInvitationMessage import PartyInvitationMessage


class PartyInvitationDungeonMessage(PartyInvitationMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        PartyInvitationMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7694
        self.vars.append({"name": "dungeonId", "type": "uint", "value": ""})
