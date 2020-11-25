from module.protocol.network.message import Message


class GameRolePlayArenaInvitationCandidatesAnswer(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3459
        self.candidates = {"type": "Vector.<LeagueFriendInformations>", "value": ""}
