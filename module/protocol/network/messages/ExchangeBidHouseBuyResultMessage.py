from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseBuyResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3583
        self.vars.append({"name": "uid", "type": "uint", "value": ""})
        self.vars.append({"name": "bought", "type": "Boolean", "value": ""})
