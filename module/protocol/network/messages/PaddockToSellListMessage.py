from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PaddockToSellListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1737
        self.pageIndex = {"type": "uint", "value": ""}
        self.totalPage = {"type": "uint", "value": ""}
        self.paddockList = {"type": "Vector.<PaddockInformationsForSell>", "value": ""}
