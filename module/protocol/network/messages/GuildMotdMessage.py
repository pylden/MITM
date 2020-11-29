from module.protocol.network.messages.SocialNoticeMessage import SocialNoticeMessage


class GuildMotdMessage(SocialNoticeMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        SocialNoticeMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8244
