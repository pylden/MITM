from module.protocol.network.message import Message


class GameRolePlayArenaInvitationCandidatesAnswer(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3459
        self.candidates = {"type": "Vector.<LeagueFriendInformations>", "value": ""}
