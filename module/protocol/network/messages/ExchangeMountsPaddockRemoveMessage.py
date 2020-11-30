from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeMountsPaddockRemoveMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9109
        self.mountsId = {"type": "Vector.<int>", "value": ""}
