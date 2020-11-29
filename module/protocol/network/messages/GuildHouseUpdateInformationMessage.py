from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildHouseUpdateInformationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6190
        self.vars.append({"name": "housesInformations", "type": "HouseInformationsForGuild", "value": ""})
