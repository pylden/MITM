from module.protocol.network.message import Message


class GameFightUpdateTeamMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8783
        self.fightId = {"type": "uint", "value": ""}
        self.team = {"type": "FightTeamInformations", "value": ""}
