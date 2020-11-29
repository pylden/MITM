from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeObjectTransfertListWithQuantityToInvMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3741
        self.vars.append({"name": "ids", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "qtys", "type": "Vector.<uint>", "value": ""})
