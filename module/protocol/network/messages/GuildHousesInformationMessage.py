from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildHousesInformationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 872
        self.housesInformations = {"type": "Vector.<HouseInformationsForGuild>", "value": ""}
