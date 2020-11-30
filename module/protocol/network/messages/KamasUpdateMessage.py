from module.protocol.network.messages.NetworkMessage import NetworkMessage


class KamasUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2022
        self.kamasTotal = {"type": "Number", "value": ""}
