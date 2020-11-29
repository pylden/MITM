from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HouseToSellListRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 259
        self.vars.append({"name": "pageIndex", "type": "uint", "value": ""})
