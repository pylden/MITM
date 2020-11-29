from module.protocol.network.messages.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage


class AllianceMotdSetRequestMessage(SocialNoticeSetRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        SocialNoticeSetRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6658
        self.vars.append({"name": "content", "type": "String", "value": ""})
