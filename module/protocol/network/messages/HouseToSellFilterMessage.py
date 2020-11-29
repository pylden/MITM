from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HouseToSellFilterMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9720
        self.vars.append({"name": "areaId", "type": "int", "value": ""})
        self.vars.append({"name": "atLeastNbRoom", "type": "uint", "value": ""})
        self.vars.append({"name": "atLeastNbChest", "type": "uint", "value": ""})
        self.vars.append({"name": "skillRequested", "type": "uint", "value": ""})
        self.vars.append({"name": "maxPrice", "type": "Number", "value": ""})
        self.vars.append({"name": "orderBy", "type": "uint", "value": ""})
