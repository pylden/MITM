from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MountFeedRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1812
        self.mountUid = {"type": "uint", "value": ""}
        self.mountLocation = {"type": "int", "value": ""}
        self.mountFoodUid = {"type": "uint", "value": ""}
        self.quantity = {"type": "uint", "value": ""}
