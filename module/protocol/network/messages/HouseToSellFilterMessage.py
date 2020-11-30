from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HouseToSellFilterMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9720
        self.areaId = {"type": "int", "value": ""}
        self.atLeastNbRoom = {"type": "uint", "value": ""}
        self.atLeastNbChest = {"type": "uint", "value": ""}
        self.skillRequested = {"type": "uint", "value": ""}
        self.maxPrice = {"type": "Number", "value": ""}
        self.orderBy = {"type": "uint", "value": ""}
