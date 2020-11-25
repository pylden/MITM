from module.protocol.network.message import Message


class GameFightUpdateTeamMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8783
        self.fightId = {"type": "uint", "value": ""}
        self.team = {"type": "FightTeamInformations", "value": ""}
