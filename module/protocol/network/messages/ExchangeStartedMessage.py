from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 954
        self.exchangeType = {"type": "int", "value": ""}
