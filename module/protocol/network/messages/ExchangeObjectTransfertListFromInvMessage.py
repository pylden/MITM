from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeObjectTransfertListFromInvMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4400
        self.vars.append({"name": "ids", "type": "Vector.<uint>", "value": ""})
