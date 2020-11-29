from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PaddockToSellFilterMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1083
        self.vars.append({"name": "areaId", "type": "int", "value": ""})
        self.vars.append({"name": "atLeastNbMount", "type": "int", "value": ""})
        self.vars.append({"name": "atLeastNbMachine", "type": "int", "value": ""})
        self.vars.append({"name": "maxPrice", "type": "Number", "value": ""})
        self.vars.append({"name": "orderBy", "type": "uint", "value": ""})
