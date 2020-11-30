from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartedTaxCollectorShopMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8259
        self.objects = {"type": "Vector.<ObjectItem>", "value": ""}
        self.kamas = {"type": "Number", "value": ""}
