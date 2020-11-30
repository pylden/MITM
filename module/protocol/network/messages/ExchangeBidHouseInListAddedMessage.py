from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseInListAddedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9210
        self.itemUID = {"type": "int", "value": ""}
        self.objectGID = {"type": "uint", "value": ""}
        self.objectType = {"type": "uint", "value": ""}
        self.effects = {"type": "Vector.<ObjectEffect>", "value": ""}
        self.prices = {"type": "Vector.<Number>", "value": ""}
