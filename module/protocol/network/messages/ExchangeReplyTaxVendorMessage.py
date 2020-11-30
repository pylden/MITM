from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeReplyTaxVendorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5635
        self.objectValue = {"type": "Number", "value": ""}
        self.totalTaxValue = {"type": "Number", "value": ""}
