from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartedTaxCollectorShopMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8259
        self.vars.append({"name": "objects", "type": "Vector.<ObjectItem>", "value": ""})
        self.vars.append({"name": "kamas", "type": "Number", "value": ""})
