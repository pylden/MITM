from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TitleSelectRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7473
        self.titleId = {"type": "uint", "value": ""}
