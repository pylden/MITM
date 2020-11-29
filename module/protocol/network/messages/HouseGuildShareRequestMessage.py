from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HouseGuildShareRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 429
        self.vars.append({"name": "houseId", "type": "uint", "value": ""})
        self.vars.append({"name": "instanceId", "type": "uint", "value": ""})
        self.vars.append({"name": "enable", "type": "Boolean", "value": ""})
        self.vars.append({"name": "rights", "type": "uint", "value": ""})
