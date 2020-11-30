from module.protocol.network.messages.NetworkMessage import NetworkMessage


class FriendSetStatusShareMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4184
        self.share = {"type": "Boolean", "value": ""}
