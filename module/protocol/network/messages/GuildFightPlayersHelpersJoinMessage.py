from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildFightPlayersHelpersJoinMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4515
        self.fightId = {"type": "Number", "value": ""}
        self.playerInfo = {"type": "CharacterMinimalPlusLookInformations", "value": ""}
