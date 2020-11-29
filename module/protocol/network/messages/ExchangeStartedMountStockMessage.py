from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartedMountStockMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6111
        self.vars.append({"name": "objectsInfos", "type": "Vector.<ObjectItem>", "value": ""})
