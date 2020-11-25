from module.protocol.network.message import Message


class GuildJoinedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7966
        self.guildInfo = {"type": "GuildInformations", "value": ""}
        self.memberRights = {"type": "uint", "value": ""}
