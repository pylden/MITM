from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HouseGuildRightsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8382
        self.vars.append({"name": "houseId", "type": "uint", "value": ""})
        self.vars.append({"name": "instanceId", "type": "uint", "value": ""})
        self.vars.append({"name": "secondHand", "type": "Boolean", "value": ""})
        self.vars.append({"name": "guildInfo", "type": "GuildInformations", "value": ""})
        self.vars.append({"name": "rights", "type": "uint", "value": ""})
