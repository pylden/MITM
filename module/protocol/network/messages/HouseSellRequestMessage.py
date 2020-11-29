from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HouseSellRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9737
        self.vars.append({"name": "instanceId", "type": "uint", "value": ""})
        self.vars.append({"name": "amount", "type": "Number", "value": ""})
        self.vars.append({"name": "forSale", "type": "Boolean", "value": ""})
