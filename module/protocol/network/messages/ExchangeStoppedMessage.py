from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeStoppedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6266
        self.id = {"type": "Number", "value": ""}
