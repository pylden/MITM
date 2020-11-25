from module.protocol.network.message import Message


class GuildMemberWarnOnConnectionStateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3164
        self.enable = {"type": "Boolean", "value": ""}
