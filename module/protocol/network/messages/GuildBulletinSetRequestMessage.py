from module.protocol.network.message import Message


class GuildBulletinSetRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2821
        self.content = {"type": "String", "value": ""}
        self.notifyMembers = {"type": "Boolean", "value": ""}
