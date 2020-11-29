from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PaddockBuyResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9413
        self.vars.append({"name": "paddockId", "type": "Number", "value": ""})
        self.vars.append({"name": "bought", "type": "Boolean", "value": ""})
        self.vars.append({"name": "realPrice", "type": "Number", "value": ""})
