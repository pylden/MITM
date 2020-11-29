from module.protocol.network.messages.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage


class AllianceBulletinSetRequestMessage(SocialNoticeSetRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        SocialNoticeSetRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8756
        self.vars.append({"name": "content", "type": "String", "value": ""})
        self.vars.append({"name": "notifyMembers", "type": "Boolean", "value": ""})
