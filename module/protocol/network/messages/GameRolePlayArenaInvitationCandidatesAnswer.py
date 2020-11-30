from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaInvitationCandidatesAnswer(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3459
        self.candidates = {"type": "Vector.<LeagueFriendInformations>", "value": ""}
