from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PaddockToSellFilterMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1083
        self.areaId = {"type": "int", "value": ""}
        self.atLeastNbMount = {"type": "int", "value": ""}
        self.atLeastNbMachine = {"type": "int", "value": ""}
        self.maxPrice = {"type": "Number", "value": ""}
        self.orderBy = {"type": "uint", "value": ""}
