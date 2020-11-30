from module.protocol.network.messages.NetworkMessage import NetworkMessage


class FriendJoinRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4174
        self.name = {"type": "String", "value": ""}
