from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SocialNoticeMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1521
        self.content = {"type": "String", "value": ""}
        self.timestamp = {"type": "uint", "value": ""}
        self.memberId = {"type": "Number", "value": ""}
        self.memberName = {"type": "String", "value": ""}
