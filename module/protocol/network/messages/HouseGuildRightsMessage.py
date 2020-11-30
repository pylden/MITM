from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HouseGuildRightsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8382
        self.houseId = {"type": "uint", "value": ""}
        self.instanceId = {"type": "uint", "value": ""}
        self.secondHand = {"type": "Boolean", "value": ""}
        self.guildInfo = {"type": "GuildInformations", "value": ""}
        self.rights = {"type": "uint", "value": ""}
