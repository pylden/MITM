from module.protocol.network.message import Message


class GuildInformationsMembersMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1702
        self.members = {"type": "Vector.<GuildMember>", "value": ""}
