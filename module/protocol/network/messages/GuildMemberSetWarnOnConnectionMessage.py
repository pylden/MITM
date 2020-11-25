from module.protocol.network.message import Message


class GuildMemberSetWarnOnConnectionMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9973
        self.enable = {"type": "Boolean", "value": ""}
