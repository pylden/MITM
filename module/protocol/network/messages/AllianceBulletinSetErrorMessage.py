from module.protocol.network.messages.SocialNoticeSetErrorMessage import SocialNoticeSetErrorMessage


class AllianceBulletinSetErrorMessage(SocialNoticeSetErrorMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        SocialNoticeSetErrorMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1895
