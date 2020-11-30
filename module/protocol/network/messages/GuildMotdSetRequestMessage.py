from module.protocol.network.messages.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage


class GuildMotdSetRequestMessage(SocialNoticeSetRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        SocialNoticeSetRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2776
        self.content = {"type": "String", "value": ""}
