from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartOkMulticraftCustomerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1363
        self.skillId = {"type": "uint", "value": ""}
        self.crafterJobLevel = {"type": "uint", "value": ""}
