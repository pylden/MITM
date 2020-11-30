from module.protocol.network.messages.NetworkMessage import NetworkMessage


class FriendsListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3107
        self.friendsList = {"type": "Vector.<FriendInformations>", "value": ""}
