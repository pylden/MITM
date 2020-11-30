from module.protocol.network.messages.NetworkMessage import NetworkMessage


class FriendStatusShareStateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9081
        self.share = {"type": "Boolean", "value": ""}
