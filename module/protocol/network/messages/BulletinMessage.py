from module.protocol.network.messages.SocialNoticeMessage import SocialNoticeMessage


class BulletinMessage(SocialNoticeMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        SocialNoticeMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5698
        self.vars.append({"name": "lastNotifiedTimestamp", "type": "uint", "value": ""})
