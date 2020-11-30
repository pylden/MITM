from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HouseSellingUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5119
        self.houseId = {"type": "uint", "value": ""}
        self.instanceId = {"type": "uint", "value": ""}
        self.secondHand = {"type": "Boolean", "value": ""}
        self.realPrice = {"type": "Number", "value": ""}
        self.buyerName = {"type": "String", "value": ""}
