from module.protocol.network.messages.NetworkMessage import NetworkMessage


class FighterStatsListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6334
        self.vars.append({"name": "stats", "type": "CharacterCharacteristicsInformations", "value": ""})
