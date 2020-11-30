from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CharacterStatsListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8872
        self.stats = {"type": "CharacterCharacteristicsInformations", "value": ""}
