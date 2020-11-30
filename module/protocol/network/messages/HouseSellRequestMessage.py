from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HouseSellRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9737
        self.instanceId = {"type": "uint", "value": ""}
        self.amount = {"type": "Number", "value": ""}
        self.forSale = {"type": "Boolean", "value": ""}
