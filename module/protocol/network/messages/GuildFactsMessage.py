from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildFactsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6652
        self.vars.append({"name": "infos", "type": "GuildFactSheetInformations", "value": ""})
        self.vars.append({"name": "creationDate", "type": "uint", "value": ""})
        self.vars.append({"name": "nbTaxCollectors", "type": "uint", "value": ""})
        self.vars.append({"name": "members", "type": "Vector.<CharacterMinimalGuildPublicInformations>", "value": ""})
