from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7113
        self.vars.append({"name": "id", "type": "uint", "value": ""})
        self.vars.append({"name": "follow", "type": "Boolean", "value": ""})
