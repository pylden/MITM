from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildFactsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6652
        self.infos = {"type": "GuildFactSheetInformations", "value": ""}
        self.creationDate = {"type": "uint", "value": ""}
        self.nbTaxCollectors = {"type": "uint", "value": ""}
        self.members = {"type": "Vector.<CharacterMinimalGuildPublicInformations>", "value": ""}
