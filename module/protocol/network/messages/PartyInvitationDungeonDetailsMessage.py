from module.protocol.network.messages.PartyInvitationDetailsMessage import PartyInvitationDetailsMessage


class PartyInvitationDungeonDetailsMessage(PartyInvitationDetailsMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        PartyInvitationDetailsMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6340
        self.dungeonId = {"type": "uint", "value": ""}
        self.playersDungeonReady = {"type": "Vector.<Boolean>", "value": ""}
