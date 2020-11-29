from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseBuyMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8882
        self.vars.append({"name": "uid", "type": "uint", "value": ""})
        self.vars.append({"name": "qty", "type": "uint", "value": ""})
        self.vars.append({"name": "price", "type": "Number", "value": ""})
