from module.protocol.network.message import Message


class GameFightRemoveTeamMemberMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6353
        self.fightId = {"type": "uint", "value": ""}
        self.teamId = {"type": "uint", "value": ""}
        self.charId = {"type": "Number", "value": ""}
