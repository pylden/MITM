from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SocialNoticeMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1521
        self.vars.append({"name": "content", "type": "String", "value": ""})
        self.vars.append({"name": "timestamp", "type": "uint", "value": ""})
        self.vars.append({"name": "memberId", "type": "Number", "value": ""})
        self.vars.append({"name": "memberName", "type": "String", "value": ""})
