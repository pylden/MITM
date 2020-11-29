from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HouseToSellListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6887
        self.vars.append({"name": "pageIndex", "type": "uint", "value": ""})
        self.vars.append({"name": "totalPage", "type": "uint", "value": ""})
        self.vars.append({"name": "houseList", "type": "Vector.<HouseInformationsForSell>", "value": ""})
