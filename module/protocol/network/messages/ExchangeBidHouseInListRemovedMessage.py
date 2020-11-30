from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseInListRemovedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6283
        self.itemUID = {"type": "int", "value": ""}
        self.objectGID = {"type": "uint", "value": ""}
        self.objectType = {"type": "uint", "value": ""}
