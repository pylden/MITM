from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7113
        self.id = {"type": "uint", "value": ""}
        self.follow = {"type": "Boolean", "value": ""}
