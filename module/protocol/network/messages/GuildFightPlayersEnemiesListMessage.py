from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildFightPlayersEnemiesListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1605
        self.fightId = {"type": "Number", "value": ""}
        self.playerInfo = {"type": "Vector.<CharacterMinimalPlusLookInformations>", "value": ""}
