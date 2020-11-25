from module.protocol.network.message import Message


class FriendsListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3107
        self.friendsList = {"type": "Vector.<FriendInformations>", "value": ""}
