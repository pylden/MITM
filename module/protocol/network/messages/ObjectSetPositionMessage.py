from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ObjectSetPositionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1317
        self.objectUID = {"type": "uint", "value": ""}
        self.position = {"type": "uint", "value": ""}
        self.quantity = {"type": "uint", "value": ""}
