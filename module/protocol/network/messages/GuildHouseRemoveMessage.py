from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildHouseRemoveMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4163
        self.vars.append({"name": "houseId", "type": "uint", "value": ""})
        self.vars.append({"name": "instanceId", "type": "uint", "value": ""})
        self.vars.append({"name": "secondHand", "type": "Boolean", "value": ""})
