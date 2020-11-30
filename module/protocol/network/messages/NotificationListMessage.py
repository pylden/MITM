from module.protocol.network.messages.NetworkMessage import NetworkMessage


class NotificationListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3042
        self.flags = {"type": "Vector.<int>", "value": ""}
