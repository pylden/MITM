from module.protocol.network.messages.NetworkMessage import NetworkMessage


class NotificationByServerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 312
        self.id = {"type": "uint", "value": ""}
        self.parameters = {"type": "Vector.<String>", "value": ""}
        self.forceOpen = {"type": "Boolean", "value": ""}
