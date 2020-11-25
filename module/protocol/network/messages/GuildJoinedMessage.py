from module.protocol.network.message import Message


class GuildJoinedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7966
        self.guildInfo = {"type": "GuildInformations", "value": ""}
        self.memberRights = {"type": "uint", "value": ""}
