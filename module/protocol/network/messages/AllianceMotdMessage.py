from module.protocol.network.messages.SocialNoticeMessage import SocialNoticeMessage


class AllianceMotdMessage(SocialNoticeMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        SocialNoticeMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1157
