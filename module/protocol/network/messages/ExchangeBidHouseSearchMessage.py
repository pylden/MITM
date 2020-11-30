from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseSearchMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6034
        self.genId = {"type": "uint", "value": ""}
        self.follow = {"type": "Boolean", "value": ""}
