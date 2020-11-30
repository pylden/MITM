from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeCraftCountRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6588
        self.count = {"type": "int", "value": ""}
