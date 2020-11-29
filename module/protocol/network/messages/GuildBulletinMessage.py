from module.protocol.network.messages.BulletinMessage import BulletinMessage


class GuildBulletinMessage(BulletinMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        BulletinMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 552
