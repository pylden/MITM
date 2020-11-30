from module.protocol.network.messages.NetworkMessage import NetworkMessage


class FriendSpouseFollowWithCompassRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 560
        self.enable = {"type": "Boolean", "value": ""}
