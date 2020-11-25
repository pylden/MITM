from module.protocol.network.message import Message


class GuildBulletinSetRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2821
        self.content = {"type": "String", "value": ""}
        self.notifyMembers = {"type": "Boolean", "value": ""}
