from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismInfoInValidMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3063
        self.reason = {"type": "uint", "value": ""}
