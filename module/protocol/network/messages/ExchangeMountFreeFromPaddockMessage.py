from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeMountFreeFromPaddockMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9283
        self.name = {"type": "String", "value": ""}
        self.worldX = {"type": "int", "value": ""}
        self.worldY = {"type": "int", "value": ""}
        self.liberator = {"type": "String", "value": ""}
