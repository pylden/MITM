from module.protocol.network.message import Message


class GuildInformationsMembersMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1702
        self.members = {"type": "Vector.<GuildMember>", "value": ""}
