from module.protocol.network.message import Message


class GameFightRemoveTeamMemberMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6353
        self.fightId = {"type": "uint", "value": ""}
        self.teamId = {"type": "uint", "value": ""}
        self.charId = {"type": "Number", "value": ""}
