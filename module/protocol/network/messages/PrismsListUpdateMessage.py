from module.protocol.network.messages.PrismsListMessage import PrismsListMessage


class PrismsListUpdateMessage(PrismsListMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        PrismsListMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8061
