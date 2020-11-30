from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightUpdateTeamMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8783
        self.fightId = {"type": "uint", "value": ""}
        self.team = {"type": "FightTeamInformations", "value": ""}
