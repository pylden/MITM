from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameContextCreateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7391
        self.context = {"type": "uint", "value": ""}
