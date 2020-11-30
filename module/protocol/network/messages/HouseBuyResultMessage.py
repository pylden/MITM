from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HouseBuyResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6050
        self.houseId = {"type": "uint", "value": ""}
        self.instanceId = {"type": "uint", "value": ""}
        self.secondHand = {"type": "Boolean", "value": ""}
        self.bought = {"type": "Boolean", "value": ""}
        self.realPrice = {"type": "Number", "value": ""}
