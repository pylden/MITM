from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeOkMultiCraftMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6926
        self.initiatorId = {"type": "Number", "value": ""}
        self.otherId = {"type": "Number", "value": ""}
        self.role = {"type": "int", "value": ""}
